from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = RichTextField()
    is_active = models.BooleanField(default=True)
    placement = models.PositiveIntegerField(blank=False, null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    
    class Meta(object):
        ordering = ['placement']