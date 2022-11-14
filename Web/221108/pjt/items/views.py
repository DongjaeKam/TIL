from django.shortcuts import render,redirect
from .models import Item
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    
    Item.objects.create(name='첫번째',type=1,price=100)
    Item.objects.create(name='테스트용',type=1,price=100)
    Item.objects.create(name='아이템',type=1,price=100)
       
    return render(request,'articles/index.html')


def search(request):
    
    search_word = request.GET.get("search-word", "Guest (or whatever)")
    
    
    
    return redirect(request,'accounts:index')
    
        
# Create your views here.
