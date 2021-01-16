from django.http import HttpResponse
from django.views.generic import View

#importing get_template from loader
from django.template.loader import get_template

#import render_to_pdf from util.py 

from HTMLtoPDF.utils import render_to_pdf 

#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('invoice.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')