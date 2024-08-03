from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_horse_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_horse_speed(self):
        ...

    @property
    @abstractmethod
    def speed_increase_after_training(self):
        ...

    def train(self):
        if self.speed + self.speed_increase_after_training > self.max_horse_speed:
            self.speed = self.max_horse_speed
        else:
            self.speed += self.speed_increase_after_training
