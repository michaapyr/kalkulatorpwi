from django.urls import path
from . import views

urlpatterns = [
    path('favicon.ico', views.favico, name='favico'),
    path('', views.index, name='index'),
    path('sections/<str:num>', views.section, name='section'),
    path('<str:num>', views.page, name='page'),
]