from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST_RATE = 4.0
    INCREASE_CLIENT_INTEREST = 2.0
    POSSIBLE_LOAN_TYPE = "MortgageLoan"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INITIAL_INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += self.INCREASE_CLIENT_INTEREST
