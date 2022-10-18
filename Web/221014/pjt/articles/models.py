from distutils.command.upload import upload
from django.db import models
from accounts.models import User


# Create your models here.
class Article(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank = True, upload_to='images')

class Comment(models.Model):
    username = models.CharField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )

    def __str__(self):
        return self.content