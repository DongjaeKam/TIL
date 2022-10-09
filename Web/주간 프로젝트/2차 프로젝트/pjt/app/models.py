from email.policy import default
from django.db import models

# Create your models here.

class review(models.Model):
    review_title = models.CharField(max_length=20)
    movie_title = models.CharField(max_length=20)
    content = models.TextField()
    grade = models.FloatField(default=10.0)