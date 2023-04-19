from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from . import models
from .models import Kredyt

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the kalkulator index.")

def index(request):

    return render(request, 'index.html')

def memory(request):
    
    template = loader.get_template('memory copy.html')
    return HttpResponse(template.render())

def section(request, num):

    if num == 1:
        template = loader.get_template('info.html')
        return HttpResponse(template.render())
    if num == 2:
        return HttpResponse("srata tata")
    else:
        return HttpResponse("błąd")