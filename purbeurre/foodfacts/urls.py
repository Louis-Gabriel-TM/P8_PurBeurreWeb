from django.urls import path

from . import views


urlpatterns = [
    path('', views.results, name='results'),
    path('details/<int:product_id>', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('my_products/', views.my_products, name='my_products'),
    path('signin/', views.signin, name='signin'),
]
