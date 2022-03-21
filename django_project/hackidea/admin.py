from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SomeModel

#from .models import Post

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(SomeModel,SomeModelAdmin)
