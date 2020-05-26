from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from .forms import StudentForm
from .models import Student 
  
def index(request):  
    student = StudentForm()
    if request.method == 'POST':
        student = StudentForm(data=request.POST)

        if student.is_valid():
            student = student.save()
            return redirect('/')
    else:
        student = StudentForm() 
    return render(request,"index.html",{'form':student})  

def list(request):
    Students = Student.objects.all()
    context = {'Students': Students}
    return render(request, 'list.html', context)
    
