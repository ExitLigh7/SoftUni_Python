from project.supply.supply import Supply


class Food(Supply):
    DEFAULT_ENERGY: int = 25

    def __init__(self, name: str, energy: int = DEFAULT_ENERGY):
        super().__init__(name, energy)
