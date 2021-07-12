from django.contrib import admin
from .models import Contact, Feedback

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name','company','email','lat','lon','phone','from_weekday', 'to_weekday','from_hour','to_hour','is_active']
    list_filters = ['name','company','from_weekday','to_weekday','from_hour','to_hour','is_active']
    search_fields = ['name']    

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email','title']
    search_fields = ['title']