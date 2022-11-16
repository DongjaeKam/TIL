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
       article = DescriptionForm(request.POST,request.FILES)
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



    # username = models.CharField(blank=True,max_length=50)
    # # item = models.ManyToManyField('items.Item', related_name='articles')
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # description = RichTextUploadingField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(blank = True, upload_to='images')

@csrf_exempt
def edit(request,pk):
    
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.title = request.POST.get('article_title')
        article.content = request.POST.get('article_content')
        article.image= request.FILES.get('article_image')
        article.save()
        
        return redirect('accounts:index')
    
    else:
    
        article = Article.objects.get(pk=pk)
        
        context ={
            
            'article': article,
            
        }
        
        
        return render(request,'articles/edit.html',context)