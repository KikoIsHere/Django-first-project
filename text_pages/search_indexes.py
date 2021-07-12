from haystack import indexes
from .models import TextPage

class TextPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    content_auto = indexes.NgramField(model_attr='title')

    def get_model(self):
        return TextPage
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def no_query_found(self):
        return self.searchqueryset.all()