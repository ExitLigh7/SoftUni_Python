from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
    MIN_PARTICIPANTS: int = 3

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CAR_TYPES:
            if self._find_car_by_model(model):
                raise Exception(f"Car {model} is already created!")

            new_car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_car = next((c for c in reversed(self.cars) if c.__class__.__name__ == car_type
                              and c.is_taken is False), None)
        if available_car is None:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = available_car
            available_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {available_car.model}."

        driver.car = available_car
        available_car.is_taken = True
        return f"Driver {driver_name} chose the car {available_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self._find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < self.MIN_PARTICIPANTS:
            raise Exception(f"Race {race_name} cannot start with less than {self.MIN_PARTICIPANTS} participants!")

        result = []
        top_3_drivers = sorted(race.drivers, key=lambda driver: driver.car.speed_limit, reverse=True)[:3]
        for winner in top_3_drivers:
            winner.number_of_wins += 1
            result.append(f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.")

        return "\n".join(result)

    # helper methods

    def _find_car_by_model(self, car_model):
        return next((c for c in self.cars if c.model == car_model), None)

    def _find_driver_by_name(self, driver_name):
        return next((d for d in self.drivers if d.name == driver_name), None)

    def _find_race_by_name(self, race_name):
        return next((r for r in self.races if r.name == race_name), None)
