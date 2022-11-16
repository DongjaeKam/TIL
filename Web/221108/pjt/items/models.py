
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from pjt import settings

# Create your models here.

class Item(models.Model):

    name = models.CharField(max_length=100)
    type = models.IntegerField(default=0)
    price = models.IntegerField (validators=[ MaxValueValidator(1000000000),MinValueValidator(100)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
     