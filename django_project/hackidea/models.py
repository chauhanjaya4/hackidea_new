from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    FASHION='fashion'
    DAILYHACKS='dailyhacks'
    ETIQUETES='etiquetes'
    HOMEDECOR='homedecor'
    HEALTH='health'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
excerpt = models.CharField(max_length=150)   
month = models.CharField(max_length=3) 
day = models.CharField(max_length=2)
content = models.TextField()
featured = models.BooleanField(default=false)
date_created = models.DateTimeField(default=datetime.now,blank=True)

def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
    #field_name = models.ImageField(blank=True,upload_to=None, height_field=None, width_field=None, max_length=100)

