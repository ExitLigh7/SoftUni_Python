from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Hyundai", "I30", 6, 60)
        self.car.fuel_amount = 30

    def test_correct_init(self):
        self.assertEqual("Hyundai", self.car.make)
        self.assertEqual("I30", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(30, self.car.fuel_amount)

    def test_make_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_larger_than_capacity_value_sets_fuel_to_capacity(self):
        self.car.refuel(70)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_with_needed_fuel_more_than_current_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(600)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_successfully_reduces_current_fuel_with_needed_fuel(self):
        self.car.drive(300)

        self.assertEqual(12, self.car.fuel_amount)


if __name__ == "__main__":
    main()
