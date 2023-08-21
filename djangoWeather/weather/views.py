from django.shortcuts import render
import json
import urllib.request
from decouple import config

def weatherapp(request):
    if request.method=="POST":
        search=request.POST['search']
        api_key=config('OPENKEY')
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+search+'&appid='+api_key).read()
        jsonData=json.loads(res)
        data={
            "country_code":str(jsonData['sys']['country']),
            "temp":str(jsonData['main']['temp'])+'k',
            "pressure":str(jsonData['main']['pressure']),
            "humidity":str(jsonData['main']['humidity'])
        }

    else:
        search=''
        data={}
    return render(request,'index.html',{'city':search,'data':data})