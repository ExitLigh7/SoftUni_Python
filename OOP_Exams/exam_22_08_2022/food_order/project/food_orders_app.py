from typing import List
from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    ADDED_MEALS: int = 0
    receipt_id: int = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        phone_duplicating = self._find_client_by_phone_number(client_phone_number)
        if phone_duplicating:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Meal):
                self.menu.append(meal)
                self.ADDED_MEALS += 1

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self._find_client_by_phone_number(client_phone_number)
        if client is None:
            self.register_client(client_phone_number)

        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        self.receipt_id += 1
        return (f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {self.ADDED_MEALS} meals on the menu and {len(self.clients_list)} clients."

    # helper methods
    def _find_client_by_phone_number(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        return client
