from django.urls import path

from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.details, name='details'),
    path('<int:product_id>/results/', views.results, name='results'),
    path('my_products/', views.my_products, name='my_products'),
]
