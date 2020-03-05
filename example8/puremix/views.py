from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):

    proj1 = Project()    
    proj1.number = 'AKAME'
    proj1.img = 'portfolio-img1.jpg'

    proj2 = Project()    
    proj2.number = 'MERANDA'
    proj2.img = 'portfolio-img2.jpg'

    proj3 = Project()    
    proj3.number = 'PULSE'
    proj3.img = 'portfolio-img3.jpg'

    proj4 = Project()    
    proj4.number = 'REA'
    proj4.img = 'portfolio-img4.jpg'

    proj5 = Project()    
    proj5.number = 'PURE MIX'
    proj5.img = 'portfolio-img5.jpg'

    proj6 = Project()    
    proj6.number = 'DINER'
    proj6.img = 'portfolio-img6.jpg'

    return render(request, "index.html", {'proj1': proj1, 'proj2': proj2,'proj3': proj3, 'proj4': proj4, 'proj5': proj5, 'proj6': proj6})
