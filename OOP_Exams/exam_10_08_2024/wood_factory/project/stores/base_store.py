from abc import ABC, abstractmethod


class BaseStore(ABC):
    MARGIN: float = 0.1
    ALLOWED_PRODUCTS: str  = ""

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 or any(char.isspace() for char in value):
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        total_price = sum(p.price for p in self.products)
        profit = total_price * self.MARGIN
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    def store_type(self):
        return self.__class__.__name__

    @abstractmethod
    def store_stats(self):
        pass
