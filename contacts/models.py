from django.db import models
from companies.models import Companie

WEEKDAYS_CHOICES = [
    ('monday',"Monday"),
    ('tuesday',"Tuesday"),
    ('wednesday',"Wednesday"),
    ('thursday',"Thursday"),
    ('friday',"Friday"),
    ('saturday',"Saturday"),
    ('sunday',"Sunday"),
]

class Contact(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Companie, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    adress = models.CharField(max_length=200)
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    from_weekday = models.CharField(max_length=50,choices=WEEKDAYS_CHOICES,unique=True)
    to_weekday = models.CharField(max_length=50,choices=WEEKDAYS_CHOICES,unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    content = models.TextField()