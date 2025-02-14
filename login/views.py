from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('<h1> insira suas infos de login</h1>')

