from django.shortcuts import render
from .models import Item
def create(request):
    
    Item.objects.create(name='첫번째',type=1,price=100)
    Item.objects.create(name='테스트용',type=1,price=100)
    Item.objects.create(name='아이템',type=1,price=100)
       
    return render(request,'articles/index.html')    
        
# Create your views here.
