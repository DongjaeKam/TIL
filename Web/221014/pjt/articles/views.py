from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect
from . import forms
from . import models
from .models import Article, Comment
from .forms import ArticleForm ,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    


    return render(request,'articles/index.html')



@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)


def reviews(request):
    articles = Article.objects.all()

    context = {

        'articles':articles,
    }

    return render(request,'articles/reviews.html',context)



def update(request):



    return render(request,'articles/index.html')



def delete(request,user_pk):

    Article.objects.get(pk=user_pk).delete()

    return render(request,'articles/index.html')


def detail(request,user_pk):

    article = Article.objects.get(pk=user_pk)
    comment_form = CommentForm()
    # template에 객체 전달
    print(len(article.comment_set.all()))
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }

    return render(request,'articles/detail.html',context)

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.username = request.user.username
        comment.save()
    
    return redirect('articles:detail', article.pk)


