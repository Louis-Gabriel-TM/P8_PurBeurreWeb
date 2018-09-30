from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    brands = models.CharField(max_length=50)
    nutriscore = models.CharField(max_length=1)
    code = models.PositiveIntegerField(unique=True)
    image_url = models.URLField()
    product_url = models.URLField(unique=True)


class SavedSubstitute(models.Model):
    id_user = models.PositiveIntegerField()
    #users = models.ManyToManyField(User)
    id_product = models.PositiveIntegerField()
    #products = models.ManyToManyFielf(Product)
    id_substitute = models.PositiveIntegerField()
    #substitutes = models.ManyToManyField(Product)
    backup_date = models.DateTimeField(auto_now_add=True)
