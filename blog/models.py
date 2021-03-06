from django.db import models
from user.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='博客分类')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = RichTextUploadingField(verbose_name='文章内容')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次更新')
    read_count = models.IntegerField(default=0, verbose_name='浏览量')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['id']
        app_label = 'blog'

    def __str__(self):
        return "<Blog: %s>" % self.title


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    author = models.CharField(verbose_name='作者', max_length=25)
    article = models.ForeignKey(to='Blog', on_delete=models.DO_NOTHING, verbose_name='评论文章')
    text = models.TextField('评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    parent_comment = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, verbose_name='父评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text


class Pic(models.Model):
    picture = models.ImageField(upload_to='img', verbose_name='图片')
