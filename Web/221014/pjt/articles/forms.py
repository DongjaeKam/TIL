
from socket import fromshare
from django import forms
from .models import article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [ 'username' , 'title' , 'content' ]