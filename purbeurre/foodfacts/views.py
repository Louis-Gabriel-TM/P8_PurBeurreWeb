from django.http import HttpResponse
from django.shortcuts import render


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


def my_products(request):
    return HttpResponse("--- MES PRODUITS ---")


def results(request):
    query = request.GET.get('query')
    return HttpResponse("""
        --- PAGE DE RESULTATS ---<br><br>
        Résultats pour la requête '{}'
        """.format(query))
