from rest_framework_json_api import serializers
from restaurant.models import Restaurant, RestaurantHours

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'menu_link', 'address','vegan','vegetarian','gluten_free','lactose_free')

class RestaurantHoursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantHours
        fields = ('restaurant', 'weekday', 'open_hour','close_hour')

