from abc import ABC, abstractmethod


class BaseClient(ABC):
    VALID_MEMBERSHIPS = ["Regular", "VIP"]
    MAX_DISCOUNT_POINTS = 100
    HALF_DISCOUNT_POINTS = 50

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.VALID_MEMBERSHIPS:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        ...

    def apply_discount(self):
        discount_percentage: int = 0
        used_points = 0
        if self.points >= self.MAX_DISCOUNT_POINTS:
            discount_percentage = 10
            used_points = self.MAX_DISCOUNT_POINTS
        elif self.points > self.HALF_DISCOUNT_POINTS:
            discount_percentage = 5
            used_points = self.HALF_DISCOUNT_POINTS

        self.points -= used_points
        return discount_percentage, self.points
