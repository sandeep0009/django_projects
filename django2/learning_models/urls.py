
from django.contrib import admin
from django.urls import path
from learnmodels.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('receipes/',receipes),
    path('delete-receips/<int:id>/',delete_receipes),
    path('login/',loginPage),
    path('register/',registerPage),
    path('logout/',logoutPage)
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
