from unittest import TestCase, main
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(TestCase):
    _VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def setUp(self):
        self.player = SoccerPlayer("Testino", 20, 2, "PSG")
        self.player.achievements = {"Best": 1}

        self.player2 = SoccerPlayer("Another", 32, 5, "Barcelona")

    def test_correct_init(self):
        self.assertEqual("Testino", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(2, self.player.goals)
        self.assertEqual("PSG", self.player.team)
        self.assertEqual({"Best": 1}, self.player.achievements)

    def test_name_setter_with_less_than_five_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Test1"

        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_age_setter_with_value_less_than_sixteen(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15

        self.assertEqual("Players must be at least 16 years of age!", str(ve.exception))

    def test_goal_setter_with_negative_value(self):
        self.player.goals = -1
        self.assertEqual(0, self.player.goals)

    def team_setter_with_invalid_team(self):
        with self.assertRaises(ValueError) as ve:
            self.player.team = "Invalid"
        expected = f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!"

        self.assertEqual(expected, str(ve.exception))

    def test_change_team_with_invalid_team_returns_error_msg(self):
        self.assertEqual("Invalid team name!", self.player.change_team("Invalid"))

    def test_change_team_successfully(self):
        self.assertEqual("Team successfully changed!", self.player.change_team("Barcelona"))
        self.assertEqual("Barcelona", self.player.team)

    def test_add_new_achievement_not_existing(self):
        achievement_name = "Fastest"
        expected = f"{achievement_name} has been successfully added to the achievements collection!"
        self.assertEqual(expected, self.player.add_new_achievement(achievement_name))
        self.assertEqual({"Best": 1, "Fastest": 1}, self.player.achievements)

    def test_add_new_achievement_existing(self):
        achievement_name = "Best"
        expected = f"{achievement_name} has been successfully added to the achievements collection!"
        self.assertEqual(expected, self.player.add_new_achievement(achievement_name))
        self.assertEqual({"Best": 2}, self.player.achievements)

    def test__lt__compares_players_by_goals_less_than_compared(self):
        expected = f"{self.player2.name} is a top goal scorer! S/he scored more than {self.player.name}."
        self.assertEqual(expected, self.player.__lt__(self.player2))

    def test__lt__compares_players_by_goals_more_than_compared(self):
        self.player.goals = 32
        expected = f"{self.player.name} is a better goal scorer than {self.player2.name}."
        self.assertEqual(expected, self.player.__lt__(self.player2))


if __name__ == "__main__":
    main()
