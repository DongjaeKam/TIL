from django.shortcuts import render

# Create your views here.

def index(request):
    
    
    context ={
        
        'hello':'hello'
        
    }
    
    return render(request,'accounts/index.html',context)


def find_password(request):
    
    
    
    context ={
        
        'stage':1
        
    }
    
    
    return render(request,'accounts/find_password.html',context)
    
    
    
    
    