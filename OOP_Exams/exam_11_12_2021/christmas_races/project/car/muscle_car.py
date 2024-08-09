from project.car.car import Car


class MuscleCar(Car):

    @property
    def min_max_speed(self):
        return 250, 450
