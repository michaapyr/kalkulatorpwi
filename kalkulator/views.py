from django.shortcuts import render #, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Likes
#from django.utils.translation import gettext as _

def index(request):
    try:
        request.session['voted']
    except:
        request.session['voted'] = False
    return render(request, 'index.html')

def memory(request):
    
    template = loader.get_template('memory copy.html')
    return HttpResponse(template.render())

def section(request, num):
    if num == 'info':
        birds = likes('')  
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted':request.session['voted']}))
    elif num == 'trivia':
        return HttpResponse(loader.get_template('trivia.html').render())
    elif num == 'index':
        return HttpResponse(loader.get_template('index2.html').render())
    elif num == 'game':
        return HttpResponse('gra start!')
    elif num == 'consent':
        request.session['consent'] = 1
        return HttpResponse('consent')
    elif num.split('__')[0] == 'like':         
        birds = likes(num.split('__')[1])    
        request.session['voted'] = 1 
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted': True}))
    else:
        try:
            template = str(num)+'.html'
            return HttpResponse(loader.get_template(template).render())
        except:
            return HttpResponse('404')

def likes(bird_name):
    birds = Likes.objects.all()
    if bird_name:
        bird = birds.get(bird = bird_name)
        likes = bird.likes + 1
        Likes.objects.filter(bird = bird_name).update(likes = likes)
    birds_table = {}
    for i in birds:
        birds_table[i.bird] = i.likes
    return birds_table
