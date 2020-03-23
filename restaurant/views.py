from django.shortcuts import render
from restaurant.models import Restaurant, RestaurantHours
from restaurant.serializers import RestaurantSerializer, RestaurantHoursSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','name']

class RestaurantHoursViewSet(viewsets.ModelViewSet):
    queryset = RestaurantHours.objects.all()
    serializer_class = RestaurantHoursSerializer

