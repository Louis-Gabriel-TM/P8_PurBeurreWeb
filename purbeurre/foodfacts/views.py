from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("--- ACCUEIL DE PUR BEURRE ---")


def details(request):
    return HttpResponse("--- PAGE DETAILLANT UN PRODUIT ---")


def disclaimer(request):
    return HttpResponse("--- MENTIONS LEGALES ---")


def my_products(request):
    return HttpResponse("--- MES PRODUITS ---")


def results(request):
    return HttpResponse("--- PAGE DE RESULTATS ---")
