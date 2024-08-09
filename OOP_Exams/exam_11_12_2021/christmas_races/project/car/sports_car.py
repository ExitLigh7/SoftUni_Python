from project.car.car import Car


class SportsCar(Car):

    @property
    def min_max_speed(self):
        return 400, 600
