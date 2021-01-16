from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=254)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country =  models.CharField(max_length=20)
    others =  models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.first_name



def get_absolute_url(self):
    return reverse('home', kwargs={'pk': self.pk})
