from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    date_hierarchy = 'created_on'


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('author_ip', 'author_user_agent')
    date_hierarchy = 'created_on'


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
