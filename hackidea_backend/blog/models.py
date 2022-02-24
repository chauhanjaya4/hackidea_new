from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

from hackidea_backend.blog.admin import BlogPostAdmin


class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    TECHNOLOGY = 'technology'
    DESIGN ='design'
    CULTURE = 'culture'
    BUSINESS = 'business'
    POLITICS = 'politics'
    OPINION = 'opinion'
    SCIENCE = 'science'
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel'

    class BlogPost(models.Model):
        title = models.CharField(max_length=50)
        slug = models.SlugField()
        category = models.CharField(max_length=50)
        thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
        excerpt = models.CharField(max_length=150)
        month = models.CharField(max_length=3)
        day = models.CharField(max_length=2)
        content = models.TextField()
        featured = models.BooleanField(default=False)
        date_created = models.DateTimeField(default=datetime.now, blank=True)

        def save(self,*args, **kwargs):
            original_slug= slugify(self.title)
            queryset = BlogPost.objects.all().filter(slug_iexact=original_slug).count()
            count=1
            slug=original_slug
            while(queryset):
                slug = original_slug + '_' + str(count)
                count += 1
                queryset = BlogPost.object.all().filter(slug_iexact=original_slug).count()

                self.slug = slug

                if self.featured:
                    try:
                        temp = BlogPost.objects.get(featured=True)
                        if self != temp: 

                        except

# Create your models here.