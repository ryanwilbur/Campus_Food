from django.contrib import admin
from .models import Restaurant, RestaurantHours

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  pass

@admin.register(RestaurantHours)
class RestaurantHoursAdmin(admin.ModelAdmin):
  pass