from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("The Terminator", 1984, 8.1)
        self.movie.actors = ["Arnold"]
        self.movie2 = Movie("Test", 2000, 9.2)

    def test_correct_init(self):
        self.assertEqual("The Terminator", self.movie.name)
        self.assertEqual(1984, self.movie.year)
        self.assertEqual(8.1, self.movie.rating)
        self.assertEqual(["Arnold"], self.movie.actors)

    def test_name_setter_with_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_with_invalid_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1885
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_who_is_not_in_list_successfully(self):
        self.movie.add_actor("Linda Hamilton")
        self.assertEqual(["Arnold", "Linda Hamilton"], self.movie.actors)

    def test_add_actor_with_already_added_actor_returns_error_msg(self):
        expected = "Arnold is already added in the list of actors!"
        self.assertEqual(expected, self.movie.add_actor("Arnold"))

    def test__gt__compares_movies_by_rating(self):
        expected = '"Test" is better than "The Terminator"'
        self.assertEqual(expected, self.movie.__gt__(self.movie2))

        self.movie2.rating = 7
        expected = '"The Terminator" is better than "Test"'
        self.assertEqual(expected, self.movie.__gt__(self.movie2))

    def test__repr__(self):
        expected = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected, self.movie.__repr__())


if __name__ == "__main__":
    main()
