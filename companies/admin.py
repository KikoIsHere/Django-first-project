from django.contrib import admin
from .models import Companie, Politic

@admin.register(Companie)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['title','slug','placement','is_active']
    list_filter = ['title','is_active']
    search_field = ['title']

@admin.register(Politic)
class PoliticsAdmin(admin.ModelAdmin):  
    list_display = ['company','title','is_active']    
    list_filter = ['is_active']
    search_field = 'title'

    