from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']

    def setUp(self):
        self.robot = Robot("11", "Military", 3, 20_000)
        self.cyborg = Robot("1", "Humanoids", 4, 18_900)

    def test_correct_init(self):
        self.assertEqual("11", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(3, self.robot.available_capacity)
        self.assertEqual(20_000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Not Valid"
        expected = f"Category should be one of '{self.ALLOWED_CATEGORIES}'"

        self.assertEqual(expected, str(ve.exception))

    def test_price_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_already_present_component_returns_error_msg(self):
        self.robot.hardware_upgrades = ["Machinegun"]
        expected = f"Robot {self.robot.robot_id} was not upgraded."

        self.assertEqual(expected, self.robot.upgrade("Machinegun", 1_000))

    def test_upgrade_successfully_increases_price(self):

        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with Machinegun.',
                         self.robot.upgrade("Machinegun", 1_000)
                         )
        self.assertEqual(["Machinegun"], self.robot.hardware_upgrades)
        self.assertEqual(21_500, self.robot.price)

    def test_update_with_less_capacity_than_needed_returns_error_msg(self):
        expected = f"Robot {self.robot.robot_id} was not updated."
        self.assertEqual(expected, self.robot.update(1.3, 4))

    def test_update_with_same_or_lower_version_as_the_one_available_returns_error_msg(self):
        expected = f"Robot {self.robot.robot_id} was not updated."
        self.robot.software_updates = [1.3]

        self.assertEqual(expected, self.robot.update(1.3, 1))
        self.assertEqual(expected, self.robot.update(1.1, 1))

    def test_update_successfully(self):
        version = 2.0
        expected = f'Robot {self.robot.robot_id} was updated to version {version}.'

        self.assertEqual(expected, self.robot.update(version, 1))

    def test_gt_with_robot_price_higher_than_compared(self):

        expected = (f'Robot with ID {self.robot.robot_id} is more expensive '
                    f'than Robot with ID {self.cyborg.robot_id}.')

        self.assertEqual(expected, self.robot.__gt__(self.cyborg))

    def test_gt_with_robot_price_equal_to_compared(self):
        self.cyborg.price = 20_000
        expected = (f'Robot with ID {self.robot.robot_id} costs equal to '
                    f'Robot with ID {self.cyborg.robot_id}.')

        self.assertEqual(expected, self.robot.__gt__(self.cyborg))

    def test_gt_with_robot_price_lower_than_compared(self):
        self.robot.price = 15_000

        expected = (f'Robot with ID {self.robot.robot_id} is cheaper '
                    f'than Robot with ID {self.cyborg.robot_id}.')

        self.assertEqual(expected, self.robot.__gt__(self.cyborg))


if __name__ == "__main__":
    main()
