from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

# Create your views here.
urlpatterns = [

   path('', views.index,name='index'),
   
]