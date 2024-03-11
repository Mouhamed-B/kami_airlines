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
    

    def test_create_10_airplanes(self):
        """
        Ensure we can create 10 airplanes from input data.
        """
        url = '/airplanes/'
        dataList:list[Airplane] = [
            {
                "id": 2,
                "passenger_capacity": 430
            },
            {
                "id": 3,
                "passenger_capacity": 330
            },
            {
                "id": 4,
                "passenger_capacity": 230
            },
            {
                "id": 5,
                "passenger_capacity": 190
            },
            {
                "id": 6,
                "passenger_capacity": 660
            },
            {
                "id": 7,
                "passenger_capacity": 710
            },
            {
                "id": 8,
                "passenger_capacity": 890
            },
            {
                "id": 9,
                "passenger_capacity": 930
            },
            {
                "id": 10,
                "passenger_capacity": 630
            },
            {
                "id": 11,
                "passenger_capacity": 530
            }
        ]
        response = self.client.post(url, dataList, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 10)
        airplanes = Airplane.objects.all()
        
        for i in range(0,10):
            self.assertEqual(airplanes[i].id, dataList[i]['id'])
            self.assertEqual(airplanes[i].passenger_capacity, dataList[i]['passenger_capacity'])
            
            fuel_tank_capacity: int = dataList[i]['id'] * 200
            fuel_consumption: float = (log10(dataList[i]['id']) * .80) + (dataList[i]['passenger_capacity']*0.002)
            max_flight_time: float = fuel_tank_capacity / fuel_consumption
            
            self.assertEqual(airplanes[i].fuel_tank_capacity, fuel_tank_capacity)
            self.assertEqual(airplanes[i].fuel_consumption, fuel_consumption)
            self.assertEqual(airplanes[i].max_flight_time, max_flight_time)

    