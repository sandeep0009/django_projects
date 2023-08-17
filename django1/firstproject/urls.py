
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.firstSetup),
    path('second/',views.secondSetup),
    path('admin/', admin.site.urls),
    path('contact/',views.contact),
    path('about/',views.about)
]
