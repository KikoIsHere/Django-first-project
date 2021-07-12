from modeltranslation.translator import register, TranslationOptions
from .models import Companie, Politic

@register(Companie)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Politic)
class PoliticTranslationOptions(TranslationOptions):
    fields = ('title', 'description')