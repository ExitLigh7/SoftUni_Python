from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Gara_Plovdiv")
        self.station.arrival_trains = deque(["Train_1", "Train_5"])
        self.station.departure_trains = deque(["Train_20", "Train_47"])

    def test_correct_init(self):
        self.assertEqual("Gara_Plovdiv", self.station.name)
        self.assertEqual(deque(["Train_1", "Train_5"]), self.station.arrival_trains)
        self.assertEqual(deque(["Train_20", "Train_47"]), self.station.departure_trains)

    def test_init_with_name_length_less_or_eq_than_three_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "not"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_appends_to_arrival_trains_que(self):
        self.station.new_arrival_on_board("Train_66")
        self.assertEqual(
            deque(["Train_1", "Train_5", "Train_66"]), self.station.arrival_trains
        )

    def test_train_has_arrived_with_other_trains_arriving_earlier(self):
        train = "Train-52"
        self.assertEqual(f"There are other trains to arrive before {train}.",
                         self.station.train_has_arrived(train)
                         )

    def test_train_has_arrived_with_first_train_to_leave(self):
        train = "Train_1"
        expected_result = f"{train} is on the platform and will leave in 5 minutes."
        self.assertEqual(expected_result, self.station.train_has_arrived(train))
        self.assertEqual(
            deque(["Train_20", "Train_47", "Train_1"]),
            self.station.departure_trains
        )


    def test_train_has_left_with_correct_first_train_pop_departure_trains(self):
        train = "Train_20"
        self.assertEqual(True, self.station.train_has_left(train))
        self.assertEqual(deque(["Train_47"]), self.station.departure_trains)

    def test_train_has_left_with_other_than_first_to_leave_train(self):
        train = "Not First"
        self.assertEqual(False, self.station.train_has_left(train))

    def test_train_has_left_without_trains_return_false(self):
        train = "No trains"
        self.station.departure_trains = deque()
        self.assertEqual(False, self.station.train_has_left(train))


if __name__ == "__main__":
    main()
