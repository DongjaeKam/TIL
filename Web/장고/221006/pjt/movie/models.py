from ipaddress import summarize_address_range
from django.db import models

# Create your models here.

class movie(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time =  models.CharField(max_length=20)