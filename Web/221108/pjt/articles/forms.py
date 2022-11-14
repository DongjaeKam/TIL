from django import forms
from .models import Article
from ckeditor.fields import RichTextField

# 만약 모델 기반이 아니라면 forms.Form
class DescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields=['title','content','description','image']
        
      