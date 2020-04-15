from django.shortcuts import render
from .models import products
# Create your views here.

def index(request):
    
    prods = products.objects.all()
    return render(request, 'index.html', {'prods':prods})
