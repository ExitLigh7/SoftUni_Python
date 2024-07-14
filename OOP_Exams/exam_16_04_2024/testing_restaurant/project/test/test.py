from unittest import TestCase, main
from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Fun Yi", 2)
        self.restaurant.waiters = \
            [{"name": "Yun To", "total_earnings": 10}]

    def test_correct_init(self):
        self.assertEqual("Fun Yi", self.restaurant.name)
        self.assertEqual(2, self.restaurant.capacity)
        self.assertEqual(
            [{"name": "Yun To", "total_earnings": 10}],
            self.restaurant.waiters)

    def test_init_with_empty_name_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_init_with_blank_name_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = "   "
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_init_with_less_than_zero_capacity_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_without_setting_filters(self):
        self.assertEqual(
            [{"name": "Yun To", "total_earnings": 10}],
            self.restaurant.get_waiters()
        )

    def test_get_waiters_with_excluding_filters(self):
        self.assertEqual(
            [],
            self.restaurant.get_waiters(min_earnings=11, max_earnings=22)
        )

    def test_add_waiter_at_max_capacity(self):
        self.restaurant.capacity = 1
        self.assertEqual("No more places!", self.restaurant.add_waiter("So-OK"))

    def test_add_waiter_with_same_name_returns_error_msg(self):
        waiter_name = "Yun To"
        self.assertEqual(
            f"The waiter {waiter_name} already exists!",
            self.restaurant.add_waiter(waiter_name)
        )

    def test_add_waiter_successfully_return_success_msg(self):
        waiter_name = "So-OK"

        self.assertEqual(
            f"The waiter {waiter_name} has been added.",
            self.restaurant.add_waiter(waiter_name)
        )

        self.assertEqual(
            [{"name": "Yun To", "total_earnings": 10}, {"name": "So-OK"}],
            self.restaurant.waiters
        )

    def test_remove_waiter_successfully_return_success_msg(self):
        waiter_name = "Yun To"
        self.assertEqual(
            f"The waiter {waiter_name} has been removed.",
            self.restaurant.remove_waiter(waiter_name)
        )

        self.assertEqual([], self.restaurant.waiters)

    def test_remove_waiter_with_not_existing_name(self):
        waiter_name = "So-OK"
        self.assertEqual(
            f"No waiter found with the name {waiter_name}.",
            self.restaurant.remove_waiter(waiter_name)
        )

    def test_total_earnings_correctly_calculate(self):

        self.assertEqual(
            sum(waiter.get('total_earnings', 0) for waiter in self.restaurant.waiters),
            self.restaurant.get_total_earnings()
        )


if __name__ == "__main__":
    main()
