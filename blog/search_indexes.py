import datetime
from haystack import indexes
from blog.models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/blog/blog_text.txt')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        """Used when the entire indexes for model is updated."""
        return self.get_model().objects.filter(created_time__lte=datetime.datetime.now())



