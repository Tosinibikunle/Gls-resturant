from rest_framework import viewsets
from .models import Resturant, MenuItem
from .serializers import ResturantSerializer, MenuItemSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Resturant.objects.all()
        serializer_class = RestaurantSerializer

        class MenuItemViewSet(viewsets.ModelViewSet):
            queryset = MenuItem.objects.all()
            serializer_class = MenuItemSerializer