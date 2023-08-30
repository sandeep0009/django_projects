from django.shortcuts import render
from users.models import *


# Create your views here.

def firstPage(request):
    return render(request,'index.html')

def Userregister(request):
    userList=Users.objects.order_by('fname')
    userdict={'users':userList}
    return render(request,'user.html',context=userdict)


