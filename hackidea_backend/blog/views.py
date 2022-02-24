from django.shortcuts import render
from django.http import HttpResponse
 
posts = [
{
     'author': 'CoreyMS',
     'title' : 'Blog Post 1',
     'content' : 'First post content',
     'date_posted' : 'August 27, 2022'
},
{
     'author': 'Jane Doe',
     'title' : 'Blog Post 2',
     'content' : 'Second post content',
     'date_posted' : 'August 28, 2022'
},

]
def index(request):
     context = {
          'posts': posts
     }
     return render(request,'blog/index.html',context)

def about(request):
     return render(request,'blog/about.html', {'title':'About'})

def posts(request):
     return HttpResponse('<h1>My Posts</h1>')

def reachme(request):
     return HttpResponse('<h1>Reach Me</h1>')

def whatsnew(request):
     return HttpResponse('<h1>Whats New</h1>')
def signup(request):
     return HttpResponse('<h1>Sign Up</h1>')     


