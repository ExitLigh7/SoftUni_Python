import requests

class BankAccount:
    def __init__(self, account_number, balance=0, currency="BGN"):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        return f"{self.balance} {self.currency}"

    def get_currency_rates(self, target_currency="USD", source_currency=None):
        """
        Method to get real-time data for currency rates from https://app.freecurrencyapi.com/dashboard.
        """
        # API endpoint URL
        url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_NbbLXUbOH2rSvzObd4Wm0SgLdexOBWMtXESqFU6y"

        try:
            # Make a GET request to the API endpoint
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Extract currency rates from the response
                currency_rates = data.get("rates")
                if currency_rates:
                    if source_currency is None:
                        source_currency = self.currency
                    if source_currency in currency_rates and target_currency in currency_rates:
                        source_rate = currency_rates[source_currency]
                        target_rate = currency_rates[target_currency]
                        conversion_rate = target_rate / source_rate
                        converted_balance = self.balance * conversion_rate
                        return f"{converted_balance:.2f} {target_currency}"
                    else:
                        print("Source or target currency not supported.")
                else:
                    print("Failed to retrieve currency rates.")
            else:
                # Print error message if the request was not successful
                print(f"Failed to retrieve currency rates. Status code: {response.status_code}")
        except Exception as e:
            # Print error message if an exception occurred during the request
            print(f"An error occurred: {e}")
        return None

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest

if __name__ == "__main__":
    bank_account = BankAccount(123456789, 1000)
    bank_account.deposit(500)
    bank_account.withdraw(200)
    print(f"Bank account balance: {bank_account.get_balance()}")

    savings_account = SavingsAccount(987654321, 2000, 5)
    savings_account.deposit(1000)
    savings_account.calculate_interest()
    print(f"Savings account balance: {savings_account.get_balance()}")

    currency_rates = bank_account.get_currency_rates(target_currency="USD", source_currency="BGN")
    if currency_rates:
        print(f"Bank account balance in {currency_rates}")
