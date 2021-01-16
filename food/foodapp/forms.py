from django import forms
from foodapp.models import Menu

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ("menu_name", "menu_desc","menu_image","menu_price" )

 
