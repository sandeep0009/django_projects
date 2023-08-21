
from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexHtml),
    path('posts/<str:pk>',posts)

]
