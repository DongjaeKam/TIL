from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
   path('', views.index,name='index'),
   path('signup/', views.signup,name='signup'),
   path('login/', views.login,name='login'),
   path('logout/', views.logout,name='logout'),
   path('delete/<int:user_pk>', views.delete ,name='delete'),
   path('<int:user_pk>', views.profile ,name='profile'),
   path('profile/<str:username>', views.profile ,name='profile'),
   path('my_profile/', views.my_profile ,name='my_profile'),
   path('my_profile/edit/', views.edit_profile ,name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)