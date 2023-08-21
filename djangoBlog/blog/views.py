from django.shortcuts import render
from .models import *

# Create your views here.

def indexHtml(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def posts(request,pk):
    posts =Post.objects.get(id=pk)
    return render(request,'posts.html',{'post':posts})
