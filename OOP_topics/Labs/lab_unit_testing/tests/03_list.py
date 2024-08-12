from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, "T", {})

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_with_non_integer_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add("T")

        self.assertEqual("Element is not Integer", str(ve.exception))
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_with_integer_element_adds_it(self):
        self.assertEqual([1, 2, 3, 8], self.int_list.add(8))

    def test_get_with_out_of_range_index(self):

        with self.assertRaises(IndexError) as ie:
            self.int_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_returns_element_on_this_idx(self):
        self.assertEqual(3, self.int_list.get(2))

    def test_insert_with_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(10, 123)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_valid_idx_and_NON_int_element(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "T")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_int_element_and_idx(self):
        expected = [1, 8, 2, 3]
        self.int_list.insert(1, 8)
        self.assertEqual(expected, self.int_list.get_data())

    def test_get_biggest_returns_correctly(self):
        self.assertEqual(3, self.int_list.get_biggest())

    def test_get_index(self):

        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == "__main__":
    main()
