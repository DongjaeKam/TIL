from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'app'


urlpatterns = [

    path('', views.index,name='index'),
    path('create/', views.create,name='create'),
    path('review/', views.detail,name='review'),
    path('delete/<int:pk>', views.delete,name='delete'),
    path('update/<int:pk>', views.update,name='update'),

]
