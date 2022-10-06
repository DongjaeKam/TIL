from socket import fromshare
from django import forms
from .models import movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = [ 'title' , 'summary' , 'running_time' ]
        
    
    
