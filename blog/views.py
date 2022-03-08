from django.shortcuts import render
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from projects.models import Project
from courses.models import Course
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.conf import settings
from akismet import Akismet
from blog.banned_words import contains_banned_words


def blog_index(request):
    posts = Post.objects.filter(publish=True).order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    try:
        Category.objects.get(name=category)
    except Category.DoesNotExist:
        return HttpResponseNotFound(f'<h1>404: "{category}" is not a valid category</h1>')

    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )

    projects = Project.objects.filter(categories__name__contains=category).order_by('title')
    courses = Course.objects.filter(categories__name__contains=category).order_by('school', 'subject', 'code')

    context = {
        'category': category,
        'posts': posts,
        'projects': projects,
        'courses': courses
    }

    return render(request, 'blog_category.html', context)


def blog_detail(request, pk, slug):
    post = Post.objects.get(pk=pk)
    return blog_detail_with_date(request, post.created_on.year, post.created_on.month, pk, slug)


def blog_detail_with_date(request, year, month, pk, slug):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            author_ip = request.META['REMOTE_ADDR']
            author_user_agent = request.META['HTTP_USER_AGENT']
            body = form.cleaned_data['body']

            if contains_banned_words(author) or contains_banned_words(body):
                return HttpResponseForbidden('<h1>Comment failed. Try being nicer.</h1>')

            akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url=settings.AKISMET_BLOG_URL)
            is_spam = akismet_api.comment_check(
                user_ip=author_ip,
                user_agent=author_user_agent,
                comment_type='comment',
                comment_author=author,
                comment_content=body
            )
            if is_spam:
                return HttpResponseForbidden('<h1>Comment failed.</h1>')

            comment = Comment(
                author=author,
                author_ip=author_ip,
                author_user_agent=author_user_agent,
                body=body,
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog_detail.html', context)
