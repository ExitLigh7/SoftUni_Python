from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()
        self.store.toy_shelf = {
            "A": "Bike",
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_correct_init(self):
        expected = {
            "A": "Bike",
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_with_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Q", "Nintendo")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_same_toy_already_in_the_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Bike")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_with_already_taken_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("C", "Nintendo")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully_adds_to_toy_shelf(self):
        self.assertEqual(f"Toy:Nintendo placed successfully!",
                         self.store.add_toy("F", "Nintendo")
                         )

        expected = {
            "A": "Bike",
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": "Nintendo",
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)

    def test_remove_toy_from_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Q", "LEGO")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_from_wrong_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "LEGO")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("B", "LEGO")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully_removes_from_toy_shelf(self):
        self.assertEqual(f"Remove toy:Bike successfully!",
                         self.store.remove_toy("A", "Bike")
                         )

        expected = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)


if __name__ == "__main__":
    main()
