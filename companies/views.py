from django.shortcuts import render
from .models import Companie, Politic
from django.views.generic import ListView, DetailView
from django import template
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView

class CompaniesView(ListView):
    model = Companie
    template_name = 'pages/companies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Companie.objects.filter(is_active=True)
        return context   

class CompaniesDetailView(DetailView):
    model = Companie
    template_name = 'pages/companies-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["politics"] = Politic.objects.filter(company=context["object"].id, is_active=True)
        return context
