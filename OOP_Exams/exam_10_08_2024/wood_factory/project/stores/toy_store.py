from itertools import groupby
from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    INITIAL_CAPACITY: int = 100
    ALLOWED_PRODUCTS: str = "Toys"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    def store_stats(self):

        sorted_toys = sorted(self.products, key=lambda t: t.model)

        toys_info = []

        for model, group in groupby(sorted_toys, key=lambda t: t.model):
            group_list = list(group)
            num_of_product_pieces = len(group_list)
            avg_price_per_model = sum(t.price for t in group_list) / num_of_product_pieces
            toys_info.append(f"{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")

        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"\
                 f"{self.get_estimated_profit()}\n"\
                 f"**Toys for sale:\n"

        result += '\n'.join(toys_info)

        return result.strip()
