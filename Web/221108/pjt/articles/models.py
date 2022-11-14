from django.db import models
from pjt import settings
from items.models import Item
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    username = models.CharField(blank=True,max_length=50)
    # item = models.ManyToManyField('items.Item', related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank = True, upload_to='images')
