from django.urls import path
from .views import blog_list, blog_detail

urlpatterns = [
    
    path('', blog_list),
    path('<id>/', blog_detail),

]
