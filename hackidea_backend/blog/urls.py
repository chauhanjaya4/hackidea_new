from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]