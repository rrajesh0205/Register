from django import forms
from .models import Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'img')
        labels = {'title': ('Title of the Blog'), 'body': ('Content of the Blog'), 'img': ('Any Image related to the Content')}
        
        