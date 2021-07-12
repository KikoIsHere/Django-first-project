from django.contrib import admin
from .models import TextPage, AboutUs, Navbar

@admin.register(TextPage)
class TextPageAdmin(admin.ModelAdmin):
    list_display = ['title','position','is_active','slug']
    list_filters = ['is_active']
    search_field = 'title'

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    exclude = ['slug']

@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ['name','position','is_active']

