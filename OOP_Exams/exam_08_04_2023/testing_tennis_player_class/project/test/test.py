from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Grisho", 33, 10)
        self.player2 = TennisPlayer("Djokovic", 37, 15)

    def test_correct_init(self):
        self.assertEqual("Grisho", self.player.name)
        self.assertEqual(33, self.player.age)
        self.assertEqual(10, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "No"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_new_win_with_non_won_tournament_name(self):
        self.player.add_new_win("ATP")
        self.assertEqual(["ATP"], self.player.wins)

    def test_add_new_win_with_already_added_name(self):
        self.player.add_new_win("ATP")
        expected = f"ATP has been already added to the list of wins!"
        self.assertEqual(expected, self.player.add_new_win("ATP"))

    def test_lt_with_points_lower_than_compared(self):
        expected = f'{self.player2.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(expected, self.player.__lt__(self.player2))

    def test_lt_with_points_higher_than_compared(self):
        self.player.points = 20
        expected = f'{self.player.name} is a better player than {self.player2.name}'
        self.assertEqual(expected, self.player.__lt__(self.player2))

    def test__str__returns_correct_string(self):
        expected = f"Tennis Player: {self.player.name}\n" \
               f"Age: {self.player.age}\n" \
               f"Points: {self.player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected, self.player.__str__())


if __name__ == "__main__":
    main()
