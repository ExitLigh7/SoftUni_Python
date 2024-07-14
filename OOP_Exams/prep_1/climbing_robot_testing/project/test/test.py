from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain", "Axe", 100, 200
        )

        self.robot_with_software = ClimbingRobot(
            "Mountain", "Axe", 100, 200
        )
        self.robot_with_software.installed_software = [
            {"name": "Cut 3s", "capacity_consumption": 20, "memory_consumption": 40},
            {"name": "arrange 3s", "capacity_consumption": 15, "memory_consumption": 30}
        ]

    def test_correct_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Axe", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_setter_category_expect_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test"

        self.assertEqual(
            f"Category should be one of {self.ALLOWED_CATEGORIES}",
            str(ve.exception)
        )

    def test_get_used_capacity(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity(self):

        expected_result = self.robot_with_software.capacity - self.robot_with_software.get_used_capacity()
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_get_used_memory(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()
        self.assertEqual(expected_result, result)

    def test_get_available_memory(self):
        expected_result = self.robot_with_software.memory - self.robot_with_software.get_used_memory()
        result = self.robot_with_software.get_available_memory()
        self.assertEqual(expected_result, result)

    def test_install_software_with_max_values(self):
        software = {"name": "arrange 3s", "capacity_consumption": 100, "memory_consumption": 200}

        self.assertEqual(
            f"Software '{software['name']}' successfully installed on {self.robot.category} part.",
            self.robot.install_software(software)
        )

    def test_install_software_with_one_param_less_than_max_values(self):
        software = {"name": "arrange 3s", "capacity_consumption": 10, "memory_consumption": 200}

        self.assertEqual(
            f"Software '{software['name']}' successfully installed on {self.robot.category} part.",
            self.robot.install_software(software)
        )

    def test_install_software_not_enough_capacity(self):
        software = {"name": "arrange 3s", "capacity_consumption": 110, "memory_consumption": 30}
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, self.robot.install_software(software))

    def test_install_software_not_enough_memory(self):
        software = {"name": "arrange 3s", "capacity_consumption": 80, "memory_consumption": 250}
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, self.robot.install_software(software))


if __name__ == "__main__":
    main()
