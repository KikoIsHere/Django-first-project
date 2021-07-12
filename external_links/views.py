from django.shortcuts import render
from django.views.generic import ListView
from .models import ExternalLink

class ExternalLinkView(ListView):
    model = ExternalLink
    template_name = 'pages/connections.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = ExternalLink.objects.filter(is_active=True)
        return context   