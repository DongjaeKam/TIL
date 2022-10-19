from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   path('', views.index,name='index'),
   path('signup/', views.signup,name='signup'),
   path('login/', views.login,name='login'),
   path('logout/', views.logout,name='logout'),
   path('delete/<int:user_pk>', views.delete ,name='delete'),
   path('<int:user_pk>', views.profile ,name='profile'),
   path('profile/', views.personal_profile ,name='personal_profile'),
   path('profile/edit/', views.edit_profile ,name='edit_profile'),
]