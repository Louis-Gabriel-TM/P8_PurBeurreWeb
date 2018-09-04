from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=100)
    brands = models.CharField(max_length=50)
    nutriscore = models.CharField(max_length=1)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class SavedSubstitute(models.Model):
    saving_date = models.DateField()
    id_product = models.IntegerField()
    id_substitute = models.IntegerField()

    def __str__(self):
        return self.saving_date
