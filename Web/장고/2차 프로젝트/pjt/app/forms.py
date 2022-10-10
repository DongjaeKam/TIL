from django import forms
from .models import review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = review
        fields = ['review_title','movie_title','content','grade']


         