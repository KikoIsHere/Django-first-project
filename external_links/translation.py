from modeltranslation.translator import register, TranslationOptions
from .models import ExternalLink

@register(ExternalLink)
class ExternalLinkTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
