from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Dune": 1}

    def test_correct_init(self):
        self.assertEqual(20, self.book_store.books_limit)
        self.assertEqual({"Dune": 1}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_books_limit_setter_with_eq_or_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.book_store.books_limit = 0

        expected = "Books limit of 0 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test__len__returns_number_of_books_in_store(self):
        self.assertEqual(1, self.book_store.__len__())

    def test__len__with_zero_books_returns_zero(self):
        self.book_store.availability_in_store_by_book_titles = {}
        self.assertEqual(0, self.book_store.__len__())

    def test_receive_book_with_not_enough_space_in_store_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("Test", 20)

        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))

    def test_receive_book_successfully_updates_quantity(self):
        book_title = "Dune"
        num_books = 4
        total_number = self.book_store.availability_in_store_by_book_titles[book_title] + num_books
        expected = f"{total_number} copies of {book_title} are available in the bookstore."

        self.assertEqual(expected, self.book_store.receive_book(book_title, num_books))

    def test_sell_book_with_unavailable_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("War", 10)

        expected = "Book War doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_with_not_enough_copies_of_that_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Dune", 3)

        expected = "Dune has not enough copies to sell. Left: 1"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_successfully(self):
        expected = "Sold 1 copies of Dune"
        self.assertEqual(expected, self.book_store.sell_book("Dune",  1))
        self.assertEqual({"Dune": 0}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(1, self.book_store.total_sold_books)

    def test__str__(self):
        expected = (f"Total sold books: {self.book_store.total_sold_books}\n"
                    f"Current availability: {len(self.book_store)}")
        for book_title, number_of_copies in self.book_store.availability_in_store_by_book_titles.items():
            expected += f"\n - {book_title}: {number_of_copies} copies"

        self.assertEqual(expected, self.book_store.__str__())


if __name__ == "__main__":
    main()
