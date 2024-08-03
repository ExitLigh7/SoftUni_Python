from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    @property
    def max_horse_speed(self):
        return 120

    @property
    def speed_increase_after_training(self):
        return 2
