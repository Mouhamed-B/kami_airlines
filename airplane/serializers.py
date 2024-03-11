from .models import Airplane
from rest_framework import serializers


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ('id', 'passenger_capacity', 'fuel_tank_capacity', 'fuel_consumption', 'max_flight_time')