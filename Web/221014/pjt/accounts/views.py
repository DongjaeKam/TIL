from genericpath import exists
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
        print("request.FILES: ",request.FILES['profile_image'])
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.profile_image =request.FILES['profile_image']
            user.save()
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





def profile(request,username):

    if username == request.user.username:
        return redirect('accounts:my_profile')


    user = get_user_model().objects.get(username=username)
    articles = user.article_set.all()
    context ={

        'articles' : articles,
        'User'  : user,
        'cnt_followings' :len(user.followings.all()),
        'cnt_follwers' : len(user.followers.all()),

    }

    return render(request,'accounts/profile.html',context)


def my_profile(request):


    user = User.objects.get(username = 'kdj1994') # 아이디가 kdj1994 인놈

    
    # request.user.followings.all() # 로그인 한놈이 팔로우 하는 놈들을 전부다 나오게
    
    if user in request.user.followings.all(): # 로그인 한놈이 팔로우 하는 놈 중에 kdj1994가 있냐?
        print("있다.")
    else:
        print("없다.")

    articles = request.user.article_set.all()

    context ={

        'articles' : articles,
        'User'  : request.user,
        'cnt_followings' :len(request.user.followings.all()),
        'cnt_follwers' : len(request.user.followers.all()),
    }

    return render(request,'accounts/profile.html',context)




def edit_profile(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST ,instance=request.user)
        if form.is_valid():
            user = form.save()  
            user.profile_image =request.FILES['profile_image']
            user.save()
            return redirect('accounts:my_profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }

    return render(request,'accounts/edit_profile.html',context)


