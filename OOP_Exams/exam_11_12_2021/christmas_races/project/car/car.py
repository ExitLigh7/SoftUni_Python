from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value
    
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    @speed_limit.setter
    def speed_limit(self, value):
        min_speed_limit, max_speed_limit = self.min_max_speed
        if not min_speed_limit <= value <= max_speed_limit:
            raise ValueError(F"Invalid speed limit! Must be between {min_speed_limit} and {max_speed_limit}!")
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_max_speed(self):
        ...
