from django.urls import path
from .views import ArticleListView, ArticleDetailView, CreatePostView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create/', CreatePostView.as_view(), name='add_post') 
]

