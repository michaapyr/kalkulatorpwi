from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sections/<str:num>', views.section, name='section'),
    path('<str:num>', views.lang, name='lang'),
]