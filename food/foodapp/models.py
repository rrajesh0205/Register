from django.db import models

# Create your models here.

class Menu(models.Model):
     menu_name = models.CharField(max_length=50)
     menu_desc = models.CharField(max_length=100)
     menu_image = models.ImageField(upload_to='pics', blank = True)
     menu_price = models.PositiveIntegerField()   