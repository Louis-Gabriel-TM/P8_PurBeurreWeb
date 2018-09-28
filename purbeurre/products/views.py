from django.http import HttpResponse, Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Product


def index(request):
    products = get_list_or_404(Product)
    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product})


def results(request, product_id):
    return HttpResponse(
        "Voici les substituts proposés pour le produit #{}.".format(
            product_id)
    )


def my_products(request):
    return HttpResponse(
        "Voici l'ensemble des produits que vous avez retenu."
    )
