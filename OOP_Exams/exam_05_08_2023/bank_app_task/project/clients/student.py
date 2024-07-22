from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST_RATE = 2.0
    INCREASE_CLIENT_INTEREST = 1.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INITIAL_INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += self.INCREASE_CLIENT_INTEREST
