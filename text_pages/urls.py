from django.urls import path
from . import views
from .views import HomeView, DetailPageView

urlpatterns = [
    path('about-us/', views.aboutus, name='about-us'),
    path('text-page-<slug>/', DetailPageView.as_view(), name='page'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('', HomeView.as_view(), name='home'),
    
    
]
