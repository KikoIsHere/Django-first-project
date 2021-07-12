from django.shortcuts import render
from django.views.generic import ListView
from .models import Question

class QuestionsView(ListView):
    model = Question
    template_name = 'pages/FAQ.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Question.objects.filter(is_active=True)
        return context       