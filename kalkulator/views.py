from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Likes
#from django.utils.translation import gettext as _

def index(request):
    try:
        lang = request.session['lang']
        if lang != 'pl':
            return redirect('/'+lang+'/start')
    except: pass
    return render(request, 'index.html',{'section':'start.html'})

def lang(request, num):
    request.session['lang'] = request.LANGUAGE_CODE
    try:
        voted = request.session['voted']
    except:
        voted = False
    try:
        template = num+'.html'
        loader.get_template(template).render()
        birds = likes('') 
        return render(request, 'index.html',{'section':template,'voted':voted, 'birds':birds})
    except:
        return render(request, 'index.html',{'section':'start.html'})

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
    elif num == 'start':
        return HttpResponse(loader.get_template('start.html').render())
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

def favico(request):
    return HttpResponse('')
