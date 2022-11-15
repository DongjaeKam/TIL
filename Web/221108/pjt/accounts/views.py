from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
from .forms import CustomUserChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import os
from articles.models import Article
import smtplib
from email.mime.text import MIMEText

# Create your views here.

def index(request):
    
    articles = Article.objects.all()
    
    context ={
        'articles':articles,        
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
  
    User =  get_user_model().objects.get(username = username)
    
    context ={
      
      'User': User,
          
    }
    
    return render(request,'accounts/profile.html',context)
        
  

@login_required
def edit_profile(request,username):
    user = get_user_model().objects.get(username=username)

    if request.user == user:

      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST ,instance=request.user)
          if form.is_valid():
              user = form.save()  
              try:
                user.profile_image =request.FILES['image']
                user.save()
              except:
                print('error')


              return redirect('accounts:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      
      context = {
          'form': form,
      }

      return render(request,'accounts/edit_profile.html',context)
    else:
      return render(request,'accounts/index.html')
    
    
    
@csrf_exempt
def find_password(request):

  f = open("D:/FindPassowordInfo.txt", 'r')

  code = f.readline()
  user = f.readline()

  # print(code,user)
  
  # f.close()
  
  # f =open("D:/FindPassowordInfo.txt", 'w')
  # code = '1\n'
  # user = '1\n'
  # f.write(code)
  # f.write(user)
  
  
  if f:
    print(1)
  else:
    print(0)

  code ='인증메세지'
  
  s = smtplib.SMTP('smtp.gmail.com', 587)
      # TLS 보안 시작
  s.starttls()
  # 로그인 인증()
  
  s.login('TravelMasterSTMP2022', 'wlyhmeupkotqyedv')
  # 보낼 메시지 설정
  
  msg = MIMEText('인증 코드 : '+ code )
  msg['Subject'] = '메일 인증 메시지'
  
  # 메일 보내기

  s.sendmail("TravelMasterSTMP2022@gmail.com",'rkaehdwo@gmail.com' , msg.as_string())
  
  # 세션 종료
  s.quit()

  return redirect('accounts:index')
  
  

  # if step == 1:

  #   context = {

  #     'step': 1,

  #   }

  #   return render(request,'accounts/find_password.html',context)
  
  # elif step == 2 :

  #   if request.method == 'POST':
      
  #     email = request.POST['email']
      
  #     print('email : ' + email )

  #     password_user = get_user_model().objects.get(email = email)

  #     # 세션 생성
  #     s = smtplib.SMTP('smtp.gmail.com', 587)
  #     # TLS 보안 시작
  #     s.starttls()
  #     # 로그인 인증()
      
  #     s.login('TravelMasterSTMP2022', 'plqkcjzguzvxkqqn')
  #     # 보낼 메시지 설정
      
      
  #     code = str(10000000 + randint(1,89999999))

  #     msg = MIMEText('인증 코드 : '+ code )
  #     msg['Subject'] = '여행 석사 메일 인증 메시지'
      
  #     # 메일 보내기
  #     if request.POST['email']:
  #       s.sendmail("TravelMasterSTMP2022@gmail.com", request.POST['email'] , msg.as_string())
      
  #     # 세션 종료
  #     s.quit()

  #   context = {

  #     'step': 2,

  #   }

  #   return render(request,'accounts/find_password.html',context)


  # elif step == 3  :
  #   _code= request.POST['code']     

  #   if _code == code :
  #     print('됬다. 인증 성공!')
  #     redirect('accounts:find_password',4)      
  #   else :
  #     context = {

  #     'step': 2,

  #     }

  #     return render(request,'accounts/find_password.html',context) 
      

  #   context = {

  #     'step': 3,

  #   }

  #   return render(request,'accounts/find_password.html',context)


  # elif step == 4 :

  #   if request.POST['password1'] == request.POST['password2']:
  #     password_user.set_password(request.POST['password1'])
  #     password_user.save()
  #     print('비밀번호 변경 가능')
  #     return redirect('accounts:login')
  #   else :
  #     print('비밀번호 변경 불가')

  #     context = {

  #     'step': 2,

  #     }

  #     return render(request,'accounts/find_password.html',context)
  