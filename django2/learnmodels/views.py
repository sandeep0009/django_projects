from django.shortcuts import render, redirect
from .models import Veggies 




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