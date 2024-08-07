from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(100)
        self.plantation.plants = {"Jo": ["Tomato"]}
        self.plantation.workers = ["Jo", "Mo"]

    def test_correct_init(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({"Jo": ["Tomato"]}, self.plantation.plants)
        self.assertEqual(["Jo", "Mo"], self.plantation.workers)

    def test_size_setter_with_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_with_already_hired_worker_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Jo")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_successfully_adds(self):
        self.assertEqual(f"Tim successfully hired.", self.plantation.hire_worker("Tim"))
        self.assertEqual(["Jo", "Mo", "Tim"], self.plantation.workers)

    def test__len__returns_count_of_plants(self):
        self.assertEqual(1, self.plantation.__len__())

    def test_planting_with_not_hired_worker_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Tim", "Onion")

        expected = "Worker with name Tim is not hired!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_with_full_plantation_raises_value_error(self):
        self.plantation.size = 1

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jo", "Onion")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_successfully_not_first_plant_case(self):
        expected = "Jo planted Onion."
        self.assertEqual(expected, self.plantation.planting("Jo", "Onion"))

    def test_planting_successfully_first_plant_case(self):
        expected = "Mo planted it's first Potato."
        self.assertEqual(expected, self.plantation.planting("Mo", "Potato"))
        self.assertEqual({"Jo": ["Tomato"], "Mo": ["Potato"]}, self.plantation.plants)

    def test__str__(self):
        expected = (f"Plantation size: {self.plantation.size}\n"
                    f"Jo, Mo")
        for worker, plants in self.plantation.plants.items():
            expected += f"\n{worker} planted: {', '.join(plants)}"
        self.assertEqual(expected, self.plantation.__str__())

    def test__repr__(self):
        expected = (f'Size: {self.plantation.size}\n'
                    f'Workers: {", ".join(self.plantation.workers)}')
        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    main()
