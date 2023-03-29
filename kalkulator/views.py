from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the kalkulator index.")

def index(request):

    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def memory(request):

    template = loader.get_template('memory.html')
    return HttpResponse(template.render())