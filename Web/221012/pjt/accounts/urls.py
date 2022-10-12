from. import views
from django.contrib import admin
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
 ]
 