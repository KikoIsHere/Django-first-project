from companies.models import Companie
from text_pages.models import TextPage, Navbar
from django.conf import settings
from django.utils import translation

def query_context_processor(request):
    companies = Companie.objects.filter(is_active=True)
    pages = TextPage.objects.filter(position='footer',is_active=True)
    links = Navbar.objects.filter(is_active=True)
    context = {
        'companies': companies,
        'pages': pages,
        'links':links,
    }

    return context