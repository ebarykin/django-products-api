from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    fields = ('name', 'description', 'price')


admin.site.register(Product, ProductAdmin)
