from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TextPage(models.Model):
    POSITION_CHOICES = (
        ('home', 'Home'),
        ('footer', 'Footer'),
    )

    title = models.CharField(max_length=50)
    description = RichTextField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES )
    upload = models.FileField(upload_to='uploads/', blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    meta_description = models.TextField(default=None)
    meta_keywords = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page', args=[str(self.slug)])

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(default='about-us')   

    def __str__(self):
        return self.title    

    @classmethod
    def object(cls):
        return cls._default_manager.all().first() 

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)



class Navbar(models.Model):

    NAME_CHOICES = (
        ('home', _('Home')),
        ('contact',_('Contacts')),
        ('companies',_('Companies')),
        ('about-us',_('About us')),
        ('faq',_('FAQ')),
        ('external-links',_('External Links')),
    )

    name = models.CharField(max_length=100, choices=NAME_CHOICES)
    position = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField()

    def get_absolute_url(self):
        return reverse(self.name)

    class Meta(object):
        ordering = ['position']