"""HTMLtoPDF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#This will import our view that we have already created
from HTMLtoPDFapp.views import GeneratePdf

urlpatterns = [
    path('admin/', admin.site.urls),

    #we have defined a  url pdf/ 
    #and whenever the user will request this url pdf,check the file urls.py inside app HTMLtoPDF.
    
    path('pdf/', GeneratePdf.as_view()), 
]