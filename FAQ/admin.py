from django.contrib import admin
from .models import Question, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','is_active','placement','category']
    list_filter = ['question','is_active','placement','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['name','is_active']