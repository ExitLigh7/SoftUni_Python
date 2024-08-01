from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self._find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!)")

        delicacy = self.VALID_DELICACIES.get(type_delicacy)
        if delicacy is None:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self._find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.VALID_BOOTHS.get(type_booth)
        if booth is None:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        suitable_booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)
        if suitable_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        suitable_booth.reserve(number_of_people)
        return f"Booth {suitable_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self._find_delicacy_by_name(delicacy_name)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_booth_by_number(booth_number)

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return (f"Booth {booth_number}:\n"
                f"Bill: {bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # helper methods

    def _find_delicacy_by_name(self, delicacy_name):
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        return delicacy

    def _find_booth_by_number(self, booth_number):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        return booth
