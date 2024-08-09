from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        pass

    def create_driver(self, driver_name: str):
        pass

    def create_race(self, race_name: str):
        pass

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass

    # helper methods

    def _find_car_by_model(self, car_model):
        pass

    def _find_driver_by_name(self, driver_name):
        pass


