from rest_framework import serializers
from .models import Resturant, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
class Meta:
   model = MenuItem
   fields = '__all__'
class ResturantSerializer(serializers.ModelSerializer):
   menu_items = MenuItemSerializer(many=True, read_only=True)
 class Meta:
    model = Resturant
    fields = '__all__'