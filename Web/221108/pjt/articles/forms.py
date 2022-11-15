from django import forms
from .models import Article
from ckeditor.fields import RichTextField
from django.forms import ModelForm, TextInput, EmailInput, NumberInput

# 만약 모델 기반이 아니라면 forms.Form
class DescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields=['title','content','image','description']
        
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '제목'
                }),
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '내용'
                }),
        }
