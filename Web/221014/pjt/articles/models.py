from distutils.command.upload import upload
from django.db import models

# Create your models here.
class article(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank = True, upload_to='images')