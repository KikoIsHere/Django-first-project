from django.db import models
from django.urls import reverse

class ExternalLink(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("external-links")
    