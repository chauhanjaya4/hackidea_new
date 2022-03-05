from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
excerpt = models.CharField(max_length=150)    
    
    #field_name = models.ImageField(blank=True,upload_to=None, height_field=None, width_field=None, max_length=100)

def __str__(self):
    return self.title 