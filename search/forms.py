from django import forms
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

class CustomSearchForm(SearchForm):

    def search(self):
        sqs = super(CustomSearchForm, self).search()
        return sqs

    def no_query_found(self):
        return self.searchqueryset.all()