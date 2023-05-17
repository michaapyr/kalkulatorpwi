from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import Likes

def index(request):
    if 'lang' in request.session:
        if request.session['lang'] != 'pl':
            return redirect('/'+request.session['lang']+'/start')
    return render(request, 'index.html',{'section':'start.html'})

def page(request, num):
    request.session['lang'] = request.LANGUAGE_CODE
    birds = likes('', request) 
    try:
        template = num + '.html'
        loader.get_template(template).render()
        return render(request, 'index.html',{'section':template,'voted':request.session['voted'], 'birds':birds})
    except:
        return redirect('/'+request.LANGUAGE_CODE+'/start')
    
def section(request, num):
    if num == 'info':
        birds = likes('', request)  
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted':request.session['voted']}))
    elif num == 'consent':
        request.session['consent'] = 1
        return HttpResponse('consent')
    elif num.split('__')[0] == 'like':     
        if not request.session['voted']:
            birds = likes(num.split('__')[1], request)  
        else:
            birds = likes('')  
        return HttpResponse(loader.get_template('info.html').render({'birds':birds, 'voted': True}))
    else:
        try:
            template = str(num)+'.html'
            return HttpResponse(loader.get_template(template).render())
        except:
            return redirect('/'+request.LANGUAGE_CODE+'/start')

def likes(bird_name, request):
    if not 'voted' in request.session:
        request.session['voted'] = False
    birds = Likes.objects.all()
    if bird_name:
        bird = birds.get(bird = bird_name)
        likes = bird.likes + 1
        Likes.objects.filter(bird = bird_name).update(likes = likes)
        request.session['voted'] = True
    birds_table = {}
    for i in birds:
        birds_table[i.bird] = i.likes
    return birds_table

def favico(request):
    return HttpResponseNotFound(":(") 
