from django.db import models
from pjt import settings
from items.models import Item
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank = True, upload_to='images')
