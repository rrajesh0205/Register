from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from . models import Article
from .forms import PostForm

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

class CreatePostView(CreateView): # new
    model = Article
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

