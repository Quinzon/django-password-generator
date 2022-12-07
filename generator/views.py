from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/Home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+-=/"))

    length = int(request.GET.get('length', 12))
    if length > 16:
        length = 16
    the_password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {"password": the_password})


def about(request):
    return render(request, 'generator/About.html')
