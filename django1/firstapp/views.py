from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstSetup(request):
     name=[
          {'name':'sandeep','age':19},
          {'name':'rohan','age':19},

          {'name':'mandi','age':139},
          {'name':'raam','age':29},
          {'name':'roy','age':59},


     ]
     return render(request,'index.html',context={'peoples':name})


def secondSetup(request):
    return HttpResponse('this is second set up')

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html') 



   
