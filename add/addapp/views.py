from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request, 'home.html', {'name': 'Rajesh'})

def add(request):
     value1 = int(request.GET['number1'])
     value2 = int(request.GET['number2'])
     res = value1 + value2
     return render(request, "result.html", {'Result':res})
