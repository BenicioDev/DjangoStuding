from django.http import HttpResponse
from django.template import loader
from .models import Membros

def membros (request):
    myMembers = Membros.objects.all().values()
    myTemplate = loader.get_template('lista_membros.html')
    context = {'myMembers': myMembers}

    return HttpResponse(myTemplate.render(context, request))