from django.shortcuts import render
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from projects.models import Project
from courses.models import Course
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.conf import settings
from akismet import Akismet


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
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


def blog_detail(request, year, month, pk, slug):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']

            akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url=settings.AKISMET_BLOG_URL)
            is_spam = akismet_api.comment_check(
                user_ip=request.META['REMOTE_ADDR'],
                user_agent=request.META['HTTP_USER_AGENT'],
                comment_type='comment',
                comment_author=author,
                comment_content=body
            )
            if is_spam:
                return HttpResponseForbidden('You are not allowed to comment.')

            comment = Comment(
                author=author,
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
