from modeltranslation.translator import register, TranslationOptions
from .models import TextPage, AboutUs, Navbar

@register(TextPage)
class TextPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description','meta_description','meta_keywords')

@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
