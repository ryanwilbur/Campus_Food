from django.shortcuts import render
from restaurant.models import Restaurant, RestaurantHours
from restaurant.serializers import RestaurantSerializer, RestaurantHoursSerializer
from rest_framework import viewsets

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantHoursViewSet(viewsets.ModelViewSet):
    queryset = RestaurantHours.objects.all()
    serializer_class = RestaurantHoursSerializer

