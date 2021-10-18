"""Module docstring"""

from car import Car
from random import randint


# CONSTANTS

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance_to_drive = randint(1, 100)
        if chance_to_drive > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
