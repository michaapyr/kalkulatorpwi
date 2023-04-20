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

    if num == 'info':
        return HttpResponse(loader.get_template('info.html').render())
    elif num == 'trivia':
        return HttpResponse(loader.get_template('trivia.html').render())
    elif num == 'index':
        return HttpResponse(loader.get_template('index2.html').render())
    elif num == 'game':
        return HttpResponse('gra start!')
    else:
        return HttpResponse("błąd zawartości")