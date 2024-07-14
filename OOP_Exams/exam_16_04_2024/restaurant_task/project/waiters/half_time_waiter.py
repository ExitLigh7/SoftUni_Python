from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 12.0

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        total_earnings = self.hours_worked * self.HOURLY_WAGE
        return total_earnings

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."
