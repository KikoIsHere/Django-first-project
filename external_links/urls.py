from django.urls import path
from .views import ExternalLinkView

urlpatterns = [
    path('', ExternalLinkView.as_view(), name='external-links')
]
