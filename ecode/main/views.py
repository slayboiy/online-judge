from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/home.html')

def about(request):
    return HttpResponse('<h1>about </h1>')

