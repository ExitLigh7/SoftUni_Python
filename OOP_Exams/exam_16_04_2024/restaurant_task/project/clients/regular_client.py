from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBERSHIP = "Regular"

    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP)

    def earning_points(self, order_amount: float):
        earned_points = int(order_amount / 10)
        self.points += earned_points
        return earned_points
