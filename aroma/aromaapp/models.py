from django.db import models

# Create your models here.

class product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_img = models.ImageField(upload_to='pics')
    prod_desc = models.TextField()
    prod_price = models.IntegerField()
