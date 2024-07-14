from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 15.0

    def calculate_earnings(self):
        return self.hours_worked * self.HOURLY_WAGE

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
