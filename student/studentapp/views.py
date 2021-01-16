from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import StudentForm
from .models import *
from django.contrib import messages

def list_and_create(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if Student.objects.filter(firstname=firstname).exists():
            messages.info(request, 'The entered Firstname has been taken')
            return redirect('index')

        else:
            form.save()
            messages.success(request, 'Student details updated.')
    return render(request, 'index.html')


def list_all(request):
    objects = Student.objects.all()
    return render(request, 'list.html', {'objects': objects})
