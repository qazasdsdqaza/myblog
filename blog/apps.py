from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '文章'


class SearchConfig(AppConfig):
    name = 'blog'
    verbose_name = '搜索'
