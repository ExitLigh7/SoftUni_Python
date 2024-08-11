from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model: str, price: float):
        super().__init__(model, price, 'Wood/Plastic', 'Toys')

    @property
    def percentage_discount(self):
        return 0.2
