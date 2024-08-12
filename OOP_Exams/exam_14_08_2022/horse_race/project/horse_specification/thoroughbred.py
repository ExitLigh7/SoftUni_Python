from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def max_horse_speed(self):
        return 140

    @property
    def speed_increase_after_training(self):
        return 3
