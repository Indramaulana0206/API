# api_app/serializers.py

from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        product = Product.objects.create(category=category, **validated_data)
        return product

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'total_price', 'created_at']
