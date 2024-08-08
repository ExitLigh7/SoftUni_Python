from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY: int = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_ENERGY)
