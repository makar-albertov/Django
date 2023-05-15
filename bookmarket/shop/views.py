from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, that is your second try, good luck!")
