from typing import List
from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        pass

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        pass

    def grant_loan(self, loan_type: str, client_id: str):
        pass

    def remove_client(self, client_id: str):
        pass

    def increase_loan_interest(self, loan_type: str):
        pass

    def increase_clients_interest(self, min_rate: float):
        pass

    def get_statistics(self):
        pass
