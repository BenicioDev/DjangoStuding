from django.http import HttpResponse
from django.template import loader

def home (request):
    template1 = loader.get_template('index.html')
    return HttpResponse(template1.render())

# Create your views here.
