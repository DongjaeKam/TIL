from email.policy import default
from django.db import models

class Todo(models.Model):
    # django 에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length = 80)
    completed = models.BooleanField(default=False)  
