from .models import Article
from django import forms



class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('first_name','last_name','phone','email','address_1','address_2','city','state','country','others','img')
        widgets = {
        'first_name' : forms.TextInput(attrs={'id': 'first_name',  'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'id': 'last_name',  'class':'form-control'}),
        'phone' : forms.TextInput(attrs={'id': 'phone',  'class':'form-control'}),
        'email' : forms.TextInput(attrs={'id': 'email',  'class':'form-control'}),
        'address_1' : forms.TextInput(attrs={'id': 'address_1',  'class':'form-control'}),
        'address_2' : forms.TextInput(attrs={'id': 'address_2',  'class':'form-control'}),
        'city' : forms.TextInput(attrs={'id': 'city',  'class':'form-control'}),
        'state' : forms.TextInput(attrs={'id': 'state',  'class':'form-control'}),
        'country' : forms.TextInput(attrs={'id': 'country',  'class':'form-control'}),
        'others' : forms.TextInput(attrs={'id': 'others',  'class':'form-control'}),
        'img' : forms. ClearableFileInput(attrs={'id': 'img',  'class':'form-control1'})
        }