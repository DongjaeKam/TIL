from django.shortcuts import render,redirect
from .models import Article
from items.models import Item
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
       item_name = request.POST.get('item')
       item = item.set().get(name=item_name)
       Article.objects.create( user = request.user , title = title,content = content , image = image , item = item  )
       return redirect('accounts:index')
    else:
       items = Item.objects.all()
       
       context ={
           
          "items" : items,
           
       }
       
       
       return render(request,'articles/create.html',context)    
        
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
    