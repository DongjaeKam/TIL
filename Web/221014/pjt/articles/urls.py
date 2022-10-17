from django.contrib import admin
from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
   path('', views.index,name='index'),
   path('create/', views.create,name='create'),
   path('reviews/', views.reviews,name='reviews'),
   path('update/', views.update,name='update'),
   path('delete/<int:user_pk>', views.delete ,name='delete'),
   path('<int:user_pk>', views.index ,name='profile'),
   path('profile/', views.index ,name='personal_profile'),
]