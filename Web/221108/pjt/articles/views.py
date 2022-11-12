from django.shortcuts import render,redirect
from .models import Article

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
def index(request):
    
    
    
    return render(request,'articles/index.html')



@csrf_exempt
def create(request):
    if request.method =='POST':
       title = request.POST.get('title')
       content = request.POST.get('content')
       image= request.FILES['image']
       Article.objects.create( user = request.user , title = title,content = content , image = image)
       return redirect('accounts:index')
    else:
       return render(request,'articles/create.html')    
        
def article_list(request,type):
    
    article_type = {
    
        'nothing' : 0,    
        'furniture' : 1 ,
        'home_appliance': 2,
        'bedding' :3,
        
    }
    
    articles = Article.objects.filter(type = article_type[type])
     
    context = {
           
       'articles':articles,
       'type':type, 
            
    } 
      
    return render(request,"articles/article_list.html",context)           
    