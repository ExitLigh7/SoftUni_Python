from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE: float = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        battery_reduction = round((mileage / self.MAX_MILEAGE) * 100)
        self.battery_level -= battery_reduction
