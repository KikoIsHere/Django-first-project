from django.db import models
from ckeditor.fields import RichTextField
import os
from django.urls import reverse

class Companie(models.Model):
    main_image = models.ImageField(upload_to='uploads/images')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    placement = models.PositiveIntegerField(blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField()
    meta_description = models.TextField(blank=False, null=True)
    meta_keywords = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.slug)])

    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Politic(models.Model):
    company = models.ForeignKey(Companie, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = RichTextField()
    file = models.FileField(upload_to='uploads/files')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.company.slug)])