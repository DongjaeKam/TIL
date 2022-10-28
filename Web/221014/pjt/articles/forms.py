
from socket import fromshare
from tokenize import Number
from django import forms
from django.forms import ModelForm , TextInput,EmailInput, NumberInput
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title' , 'content','image','type_of_article']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'content' ]

        widgets = {
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%; margin : 2px; ',
            }),
        }



# class UserInfoForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'age']
#         widgets = {
#             'name': TextInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Name'
#                 }),
#             'email': EmailInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Email'
#                 }),
#             'age': NumberInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 100px;',
#                 'placeholder': 'Age'
#             }),
#         }