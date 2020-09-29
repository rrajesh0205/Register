from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy  
from .forms import StudentForm
from .models import Student 

  


def list_and_create(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    # notice this comes after saving the form to pick up new objects
    objects = Student.objects.all()
    return render(request, 'index.html', {'objects': objects, 'form': form})
    