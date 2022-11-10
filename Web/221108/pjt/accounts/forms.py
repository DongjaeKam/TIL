from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", 'first_name', 'last_name',"profile_image"]

class CustomUserChangeForm(UserChangeForm):
      class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
    