from django.db import models
from django.urls import reverse
from math import log10
# Create your models here.

class Airplane(models.Model):

    id:int = models.IntegerField(verbose_name="id",primary_key=True,auto_created=False)
    passenger_capacity:int = models.IntegerField(blank=False)

    @property
    def fuel_tank_capacity(self) -> int:
        return self.id * 200
    
    @property
    def fuel_consumption(self) -> float:
        return (log10(self.id) * .80) + (self.passenger_capacity*0.002)
    
    @property
    def max_flight_time(self) -> float:
        return self.fuel_tank_capacity / self.fuel_consumption

    class Meta:
        verbose_name:str = ("airplane")
        verbose_name_plural:str = ("airplanes")
