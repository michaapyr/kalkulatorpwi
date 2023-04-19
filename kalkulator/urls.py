from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memory', views.memory, name='memory'),
    path("sections/<int:num>", views.section, name='section'),
]