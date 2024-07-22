from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.van_car = (
            SecondHandCar(
                "Honda FR-V",
                "mini van",
                200,
                8000
            ))

        self.car = SecondHandCar(
            "Hyundai I30",
            "hatch bag",
            101,
            12000
        )
        self.car.repairs = ["ABS module"]

    def test_correct_init(self):
        self.assertEqual("Honda FR-V", self.van_car.model)
        self.assertEqual("mini van", self.van_car.car_type)
        self.assertEqual(200, self.van_car.mileage)
        self.assertEqual(8000, self.van_car.price)
        self.assertEqual([], self.van_car.repairs)

    def test_price_setter_returns_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.van_car.price = 1.0

        self.assertEqual(
            'Price should be greater than 1.0!',
            str(ve.exception)
        )

    def test_mileage_setter_returns_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.van_car.mileage = 100

        self.assertEqual(
            'Please, second-hand cars only! Mileage must be greater than 100!',
            str(ve.exception)
        )

    def test_set_promotional_price_with_higher_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.van_car.set_promotional_price(8001.0)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_lower_price_expect_success(self):
        self.assertEqual(
            'The promotional price has been successfully set.',
            self.van_car.set_promotional_price(7800.0)
        )
        self.assertEqual(7800.0, self.van_car.price)

    def test_need_repair_with_high_repair_price_returns_error_msg(self):
        self.assertEqual(
            'Repair is impossible!',
            self.van_car.need_repair(4100, "Clutch and turbo")
        )

    def test_need_repair_with_price_lower_than_half_of_car_price(self):
        self.assertEqual(
            f'Price has been increased due to repair charges.',
            self.van_car.need_repair(850, "Brakes")
        )
        self.assertEqual(8850.0, self.van_car.price)
        self.assertEqual(["Brakes"], self.van_car.repairs)

    def test_gt_with_different_car_types_returns_error_msg(self):
        self.assertEqual(
            'Cars cannot be compared. Type mismatch!',
            self.van_car.__gt__(self.car)
        )

    def test_gt_with_same_car_types_expect_shows_if_car_is_with_higher_price_than_other(self):
        self.van_car.car_type = "hatch bag"
        self.assertEqual(False, self.van_car.__gt__(self.car))

    def test_correct_str(self):
        expected = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(expected, self.car.__str__())


if __name__ == "__main__":
    main()
