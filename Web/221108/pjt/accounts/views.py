from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import os

# Create your views here.

def index(request):
    
    
    context ={
        
        'hello':'hello'
        
    }
    
    return render(request,'accounts/index.html',context)


def find_password(request):
    
    
    
    context ={
        
        'stage':1
        
    }
    
    
    return render(request,'accounts/find_password.html',context)

@csrf_exempt
def login(request):
  
  if request.user.is_authenticated:
    
    return render(request, 'articles/index.html')

  else:

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login') 
    
@csrf_exempt
def signup(request):
  if request.method == 'POST':
    sign_form = UserForm(request.POST, request.FILES)
    if sign_form.is_valid():
      sign = sign_form.save()
      os.mkdir("./media/userfiles/"+sign.username)
      auth_login(request, user=sign)
      return redirect('accounts:index')
  else:
    sign_form = UserForm()

  context = {
    'sign_form' : sign_form,
  }
  
  return render(request, 'accounts/signup.html', context)

def user_list(request):
    
    users = get_user_model().objects.all()
    
    context ={
        
        'users' : users,
        
    }
    
    return render(request,'accounts/user_list.html',context)

def delete(request,pk):
    
  user = get_user_model().objects.get(pk=pk).delete()

  return redirect('accounts:index')
  
def profile(request,username):
  
  
  if get_user_model().objects.get(username = username):
    
    User =  get_user_model().objects.get(username = username)
    
    print('hello')
    
    context ={
      
      'User': User,
          
    }
        
  else:
    print('bye')
    
    context ={
      
      'User ': "없음",
          
    }
    
  return render(request,'accounts/profile.html',context)