from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        

        return redirect('/')
    else:
        return render(request, 'add.html')