from django.contrib import admin

from .models import Category, Product, SavedSubstitute


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SavedSubstitute)
