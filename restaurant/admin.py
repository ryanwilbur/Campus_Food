from django.contrib import admin
from .models import Restaurant, RestaurantHours


class RestaurantHoursInline(admin.TabularInline):
    model = RestaurantHours
    extra = 1

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  inlines = [RestaurantHoursInline,]
