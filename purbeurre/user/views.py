from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignInForm, LogInForm


def login(request):
    form = LogInForm()
    return HttpResponse("--- SE CONNECTER ---")


def signin(request):
    form = SignInForm()
    return HttpResponse("--- CREATION DE COMPTE ---")
