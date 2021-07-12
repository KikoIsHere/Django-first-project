from django.conf.urls import url
from haystack.views import SearchView
from django.urls import path
from . import views


urlpatterns = [
    path('results', views.results, name='results'),
    path('search', views.autocomplete, name='autocomplete')
]