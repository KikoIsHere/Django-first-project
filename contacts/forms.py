from django.forms import ModelForm
from .models import Feedback
from django import forms
from django.utils.translation import ugettext as _

class FeedbackForm(ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':_('First Name')}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': _('Last Name')}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': _('Title')}))
    content = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder': _('Message')}))

    class Meta:
        model = Feedback
        fields = ['first_name','last_name','email','title','content']

