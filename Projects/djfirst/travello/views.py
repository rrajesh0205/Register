from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Chennai'
    dest1.desc = 'The Gateway of the South India'
    dest1.img = 'destination_1.jpg'
    dest1.price = 499

    dest2 = Destination()
    dest2.name = 'Bengaluru'
    dest2.desc = 'The City of Gardens'
    dest2.img = 'destination_2.jpg'
    dest2.price = 599

    dest3 = Destination()
    dest3.name = 'Sunderbans'
    dest3.desc = 'For its enigmatic wilderness'
    dest3.img = 'destination_3.jpg'
    dest3.price = 799

    dest4 = Destination()
    dest4.name = 'Kerala'
    dest4.desc = 'For its backwaters and much more'
    dest4.img = 'destination_4.jpg'
    dest4.price = 1099
    

    dest5 = Destination()
    dest5.name = 'Andaman & Nicobar'
    dest5.desc = 'For its pristine beauty and array of water sports'
    dest5.img = 'destination_5.jpg'
    dest5.price = 1299

    dest6 = Destination()
    dest6.name = 'Varanasi'
    dest6.desc = 'For its spiritual essence'
    dest6.img = 'destination_6.jpg'
    dest6.price = 999
    

    return render(request, "index.html",{'dest1':dest1, 'dest2':dest2, 'dest3':dest3, 'dest4':dest4, 'dest5':dest5, 'dest6':dest6})
