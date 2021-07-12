from django.contrib import admin
from .models import ExternalLink

@admin.register(ExternalLink)
class ExternalLinksAdmin(admin.ModelAdmin):
    list_display = ['title','link','is_active']
    list_filter = ['title','is_active']
    search_field = ['title']    
