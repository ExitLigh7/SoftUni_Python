from project.divers.base_diver import BaseDiver

class ScubaDiver(BaseDiver) :
    INITIAL_OXYGEN = 540
    OXYGEN_REDUCTION = 0.3

    def __init__(self, name: str) :
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int) :
        needed_oxygen = int(self.OXYGEN_REDUCTION * time_to_catch)

        if self.oxygen_level >= needed_oxygen :
            self.oxygen_level -= needed_oxygen
        else:
            self.oxygen_level = 0

    def renew_oxy(self) :
        self.oxygen_level = self.INITIAL_OXYGEN