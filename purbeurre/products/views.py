from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Bienvenue sur l'index de l'App Products.")
