from django.shortcuts import render, redirect
from .models import Veggies 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout




def home(request):
    return render(request ,'index.html')



def receipes(request):
    if request.method=="POST" :
        data = request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        Veggies.objects.create(
            receipe_image= receipe_image,
            receipe_name=receipe_name,
            receipe_description= receipe_description

        )
        return redirect('/receipes')
    
    queryset=Veggies.objects.all()
    context={'receipes':queryset}
    return render(request,'receipes.html',context)


def delete_receipes(request ,id):
    queryset=Veggies.objects.get(id=id)
    queryset.delete()


    return redirect('/receipes')

""" login """
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid')
            redirect('/login/')

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipes/')
    return render(request,'login.html')

# logout

def logoutPage(request):
    logout(request)
    return redirect('/login/')

def registerPage(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"user exist")
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()
        messages.info(request,"successful")
        return redirect('/register/')
    return render(request,'register.html')