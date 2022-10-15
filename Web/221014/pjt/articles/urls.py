from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
   path('', views.index,name='index'),
   path('signup/', views.index,name='signup'),
   path('login/', views.index,name='login'),
   path('logout/', views.index,name='logout'),
   path('delete/<int:user_pk>', views.index ,name='delete'),
   path('<int:user_pk>', views.index ,name='profile'),
   path('profile/', views.index ,name='personal_profile'),
]