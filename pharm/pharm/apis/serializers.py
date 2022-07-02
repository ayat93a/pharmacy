from dataclasses import fields
from pyexpat import model
from rest_framework import serializers 
from pharm.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['id' ,'product_name' ,'days_to_supply','last_order_quantity', 'available_quantity' ,'cost_per_item',
        'price_per_item', 'discount' , 'bonus' , 'bonus_quantity' , 'total_cost' , 'total_price' , 'profit_per_item',
        'total_profit']
        model = Product