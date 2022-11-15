from django.shortcuts import render,redirect
from .models import Article
from items.models import Item
from .forms import DescriptionForm

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
def index(request):
    
    
    
    return render(request,'articles/index.html')



@csrf_exempt
def create(request):
    if request.method =='POST':
      #  item = item.set().get(name=item_name)
       article = DescriptionForm(request.POST)
       print('aaaa')
       article.username = request.user.username
       article.save()

       return redirect('accounts:index')
    else:
       items = Item.objects.all()
       form = DescriptionForm() 
       
       context ={
           
          "items" : items,
          "form":form,
           
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
 
@csrf_exempt
def search(request):
    
        all_articles = Article.objects.all()
        
        
        for article in all_articles:
            print(article.title , article.content)
        
    
        if request.method == 'POST':
               search = request.POST['search']
               print(search)          
               items = Item.objects.filter(name__contains=search)
               articles_by_title = Article.objects.filter(title__contains=search)
               for article in articles_by_title:
                    print(article.title , article.content)
               articles_by_content = Article.objects.filter(content__contains=search)
               for article in articles_by_content:
                    print(article.title , article.content)
              
               context = {
                   'search': search, 
                   'items':items,
                   'articles_by_title':articles_by_title,
                   'articles_by_content':articles_by_content,
                   
                   
               }
               return render(request, 'articles/search.html',context)
        else:
               return redirect('accounts:index')


