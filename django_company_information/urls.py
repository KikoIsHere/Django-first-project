"""django_company_information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from django.contrib.sitemaps.views import sitemap
from .sitemaps import CompanySitemap, PoliticSitemap, HomeTextPageSitemap, ExternalLinksSitemap, CompanyDetailsSitemap
sitemaps = {
    'companies':CompanySitemap,
    'politics': PoliticSitemap,
    'text-pages':HomeTextPageSitemap,
    'company-detail':CompanyDetailsSitemap,
    'external-links':ExternalLinksSitemap
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('companies/', include('companies.urls')),
    path('contacts/', include('contacts.urls')),
    path('external_links/', include('external_links.urls')),
    path('faq/', include('FAQ.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    url(r'^search/', include('search.urls')),
    path('', include('text_pages.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('', include('text_pages.urls')),
    path('companies/', include('companies.urls')),
    path('contacts/', include('contacts.urls')),
    path('external_links/', include('external_links.urls')),
    path('faq/', include('FAQ.urls')),)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]