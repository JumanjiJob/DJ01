from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой ghfпервый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница проекта на Django</h1>")

def data(request):
    return HttpResponse("<h1>Содержимое страницы data</h1>")

def test(request):
    return HttpResponse("<h1>Содержимое страницы test</h1>")