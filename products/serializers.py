from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительным числом.")
        return value

    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Продукт с таким названием уже существует.")
        return value
