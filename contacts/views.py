from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from .models import Contact
from .forms import FeedbackForm
from django.core.mail import EmailMessage
from django.conf import settings

def contact(request):
    form = FeedbackForm()
    contacts = Contact.objects.filter(is_active=True)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            #make email to be edited in admin
            msg = EmailMessage(form.cleaned_data['title'], form.cleaned_data['content'], form.cleaned_data['email'], [settings.LIST_OF_EMAIL_RECIPIENTS])
            msg.send()
            form.save()
            return redirect('contact')
        #add form error print
    context = {
        'form':form,
        'contacts':contacts,
    }
    return render(request ,'pages/contacts.html', context)
