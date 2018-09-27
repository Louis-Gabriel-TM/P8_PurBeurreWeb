from django.urls import path

from . import views


urlpatterns = [
    path('details/', views.details, name='details'),
    path('my_products/', views.my_products, name='my_products'),
    path('', views.results, name='results'),
]
