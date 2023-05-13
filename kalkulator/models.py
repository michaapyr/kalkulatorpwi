from django.db import models

# Create your models here.

class Kredyt(models.Model):
    name = models.CharField(max_length=10)

class KredytWynik(models.Model):
    kredyt = models.ForeignKey('Kredyt', on_delete=models.CASCADE)
    suma = models.DecimalField(max_digits=10,decimal_places=2)

class Likes(models.Model):
    bird = models.CharField(max_length=250, unique=True)
    likes = models.IntegerField()