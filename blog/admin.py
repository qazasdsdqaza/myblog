from django.contrib import admin
from blog.models import Blog, BlogType


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'created_time', 'updated_time', 'author', 'read_count')


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
