from django.shortcuts import render,redirect
from . import forms
from . import models
from .models import article
from .forms import ArticleForm

# Create your views here.

def index(request):

    


    return render(request,'articles/index.html')




def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)


def read(request):



    return render(request,'articles/index.html')



def update(request):



    return render(request,'articles/index.html')



def delete(request,user_pk):



    return render(request,'articles/index.html')