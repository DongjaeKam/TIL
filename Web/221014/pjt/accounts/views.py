from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm , CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from articles.models import Article
from accounts.models import User


# Create your views here.


def index(request):

    users = get_user_model().objects.all()

    context = {

        'users' : users,

    }

    return render(request,'accounts/index.html',context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user)
            print(f'user : {user.id}') 
            return redirect('articles:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')



def delete(request,user_pk):

    user = get_user_model().objects.get(pk=user_pk)
    user.delete()

    return redirect('accounts:index')


def profile(request,user_pk):



    return render(request)


def personal_profile(request):

    articles = request.user.article_set.all()

    context ={

        'articles' : articles

    }

    return render(request,'accounts/profile.html',context)




def edit_profile(request):

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:profile')
    else:
        form = CustomUserChangeForm(instance = request.user)
        print('hihihi')
    
    context = {
        'form': form
    }

    return render(request,'accounts/edit_profile.html',context)