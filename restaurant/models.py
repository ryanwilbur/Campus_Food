from django.db import models

from django.contrib.auth.models import User


class Restaurant(models.Model):
  name = models.CharField(max_length=200)
  menu_link = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  vegan = models.BooleanField(default=False, null=True)
  vegetarian = models.BooleanField(default=False, null=True)
  gluten_free = models.BooleanField(default=False, null=True)
  lactose_free = models.BooleanField(default=False, null=True)
  
  def __str__(self):
    return self.name

WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]

class RestaurantHours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True
    )
    open_hour = models.TimeField()
    close_hour = models.TimeField()

    def __str__(self):
        return self.restaurant

    class Meta:
        verbose_name = 'RestaurantHours'
        verbose_name_plural = 'RestaurantHours'
