from project.stores.base_store import BaseStore
from itertools import groupby


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY: int = 50
    ALLOWED_PRODUCTS: str = "Furniture"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    def store_stats(self):
        sorted_furniture = sorted(self.products, key=lambda f: f.model)

        furniture_info = []

        for model, group in groupby(sorted_furniture, key=lambda f: f.model):
            group_list = list(group)
            num_of_product_pieces = len(group_list)
            avg_price_per_model = sum(f.price for f in group_list) / num_of_product_pieces
            furniture_info.append(f"{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")

        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n" \
                 f"{self.get_estimated_profit()}\n" \
                 f"**Furniture for sale:\n"
        result += '\n'.join(furniture_info)

        return result.strip()
