from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.views.generic import ListView, DetailView
from .models import TextPage, AboutUs
from django.utils import translation
from companies.models import Companie, Politic
from django.urls import translate_url
from django.http import HttpResponseRedirect, response
import re

def sitemap(request):
    companies = Companie.objects.all()
    politcs = Politic.objects.all()
    text_pages = TextPage.objects.all()
    context = {
        'companies':companies,
        'politcs':politcs,
        'text_pages':text_pages,
    }
    return render(request, 'pages/sitemap.html',context)


class HomeView(ListView):
    model = TextPage
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = TextPage.objects.filter(position='home', is_active=True)
        return context    

class DetailPageView(DetailView):
    model = TextPage
    template_name = 'pages/about-us.html'


def aboutus(request):
    elements = AboutUs.objects.get()
    context = {
        'object':elements
    }
    return render(request, 'pages/about-us.html', context)
