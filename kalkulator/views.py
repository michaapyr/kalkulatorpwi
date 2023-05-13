from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Likes
#from django.utils.translation import gettext as _

def index(request):
    lang = 'pl'
    try:
        lang = request.session['lang']
    except: pass
    return redirect('/'+lang+'/index')
    #return render(request, 'index.html',{'section':'index'})

def lang(request, num):
    request.session['lang'] = request.LANGUAGE_CODE
    return render(request, 'index.html',{'section':num})

def section(request, num):
    try:
        voted = request.session['voted']
    except: 
        voted = False
        request.session['voted'] = voted
    if num == 'info':
        birds = likes('')  
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted':voted}))
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
        if not request.session['voted']:
            birds = likes(num.split('__')[1])  
            request.session['voted'] = True  
        else:
            birds = likes('')  
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted': True}))
    else:
        try:
            template = str(num)+'.html'
            return HttpResponse(loader.get_template(template).render())
        except:
            return HttpResponse('')

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
