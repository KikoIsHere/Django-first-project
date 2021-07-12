from django.urls import path
from .views import CompaniesView, CompaniesDetailView
from django.conf.urls import url

urlpatterns = [
    path('', CompaniesView.as_view(), name='companies'),
    path('company-detail-<slug>', CompaniesDetailView.as_view(), name='company-detail'),
]