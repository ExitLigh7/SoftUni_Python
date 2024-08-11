from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    def __init__(self, model: str, price: float):
        super().__init__(model, price, 'Wood', 'Furniture')

    @property
    def percentage_discount(self):
        return 0.1

