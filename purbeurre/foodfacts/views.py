from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import SignInForm, LogInForm


def index(request):
    return HttpResponse("--- ACCUEIL DE PUR BEURRE ---")


def connect(request):
    error = False

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse(index))
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'foodfacts/login.html', locals())


def details(request, product_id):
    id = int(product_id)
    return HttpResponse("""
        --- PAGE DETAILLANT UN PRODUIT ---<br><br>
        Détails du produit d'identifinat {}
        """.format(id))


def disclaimer(request):
    return HttpResponse("--- MENTIONS LEGALES ---")


def disconnect(request):
    logout(request)
    return redirect(reverse(index))


@login_required(login_url='/foodfacts/login')
def my_products(request):
    return HttpResponse("--- MES PRODUITS ---")


def results(request):
    query = request.GET.get('query')
    return HttpResponse("""
        --- PAGE DE RESULTATS ---<br><br>
        Résultats pour la requête '{}'
        """.format(query))


def signin(request):
    error = ""

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            #email_confirm = form.cleaned_data['email_confirm']
            email = ""
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password_confirm != password:
                error = "Les mots de passe ne concordent pas"
            # elif email_confirm != email:
                #error = "Les emails ne concordent pas"
            else:
                user = authenticate(username=username, password=password)
                if user:
                    error = "Ce compte existe déjà"
                else:
                    User.objects.create_user(username, email, password)
                    return redirect(reverse(index))
    else:
        form = SignInForm()

    return render(request, 'foodfacts/signin.html', locals())
