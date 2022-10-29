from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect
from . import forms
from . import models
from .models import Article, Comment,Like
from accounts.models import User
from .forms import ArticleForm ,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    article = Article.objects.get(id=8)

    context ={

        'article':article,
    }
    

    return render(request,'articles/index.html',context)

@login_required
def create(request):
    if request.method == 'POST':

        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            image = request.FILES['image']
            user = request.user
            title = request.POST.get('title')
            content = request.POST.get('content')
            Article.objects.create(image= image, user = user , title=title, content=content)
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
 


def delete(request,article_pk):

    Article.objects.get(pk=article_pk).delete()

    return redirect('accounts:my_profile')


def detail(request,article_pk):

    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    
    # template에 객체 전달
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
        'like': Like.objects.filter(article = article , user = request.user),
        'like_cnt': len(Like.objects.filter(article = article)), 
    }

    return render(request,'articles/detail.html',context)

@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.username = request.user.username
        comment.save()
    
    return redirect('articles:detail', article.pk)



def reviews_like(request,article_pk):

    article = Article.objects.get(pk = article_pk )
    
    like = Like.objects.filter(article = article, user = request.user)

    if like :
        like.delete()
    else:
        Like.objects.create(article = article, user = request.user )

    return  redirect('articles:detail', article_pk)


def main_like(request,article_pk):

    article = Article.objects.get(pk = article_pk )
    
    like = Like.objects.filter(article = article, user = request.user)

    if like :
        like.delete()
    else:
        Like.objects.create(article = article, user = request.user )

    return  redirect('articles:main', article_pk)
