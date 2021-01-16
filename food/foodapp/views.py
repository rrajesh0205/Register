from . models import Menu
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy 
from foodapp.forms import MenuForm

# Create your views here.


class ModelListView(ListView):
    model = Menu
    template_name = "home.html"

class ModelCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = "post.html"
    success_url = reverse_lazy('home')
    
