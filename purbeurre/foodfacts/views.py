from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import SignInForm, LogInForm


def index(request):
    return HttpResponse("--- ACCUEIL DE PUR BEURRE ---")


def details(request, product_id):
    id = int(product_id)
    return HttpResponse("""
        --- PAGE DETAILLANT UN PRODUIT ---<br><br>
        Détails du produit d'identifinat {}
        """.format(id))


def disclaimer(request):
    return HttpResponse("--- MENTIONS LEGALES ---")


def login(request):
    form = LogInForm()
    template = loader.get_template('foodfacts/login.html')
    return HttpResponse(template.render(request=request))


def my_products(request):
    return HttpResponse("--- MES PRODUITS ---")


def results(request):
    query = request.GET.get('query')
    return HttpResponse("""
        --- PAGE DE RESULTATS ---<br><br>
        Résultats pour la requête '{}'
        """.format(query))


def signin(request):
    form = SignInForm()
    template = loader.get_template('foodfacts/signin.html')
    return HttpResponse(template.render(request=request))
