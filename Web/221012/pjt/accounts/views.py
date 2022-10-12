from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login



# Create your views here.

def index(request):

    return render(request,'accounts/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request,'accounts/signup.html')

def signup(request):

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()

    context = {

        'form': form
    }

    return render(request,'accounts/index.html')