from math import log10
from django.urls import reverse
from airplane.models import Airplane
from rest_framework import status
from rest_framework.test import APITestCase

class AirplaneTests(APITestCase):
    
    def test_create_single_airplane(self):
        """
        Ensure we can an airplane from input data.
        """
        url = '/airplanes/'
        data:Airplane = {
            "id": 1,
            "passenger_capacity": 530
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)
        airplane:Airplane = Airplane.objects.get()
        self.assertEqual(airplane.id, data['id'])
        self.assertEqual(airplane.passenger_capacity, data['passenger_capacity'])
        
        fuel_tank_capacity: int = data['id'] * 200
        fuel_consumption: float = (log10(data['id']) * .80) + (data['passenger_capacity']*0.002)
        max_flight_time: float = fuel_tank_capacity / fuel_consumption
        
        self.assertEqual(airplane.fuel_tank_capacity, fuel_tank_capacity)
        self.assertEqual(airplane.fuel_consumption, fuel_consumption)
        self.assertEqual(airplane.max_flight_time, max_flight_time)
    
    