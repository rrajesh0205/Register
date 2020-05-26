from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request, 'home.html', {'name': 'Rajesh'})

def add(request):
     value1 = int(request.POST['number1'])
     value2 = int(request.POST['number2'])
     res = value1 + value2
     return render(request, "result.html", {'Result':res})
