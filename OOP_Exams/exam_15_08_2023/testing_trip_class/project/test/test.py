from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(6300.0, 2, False)
        self.trip_booked_dest = Trip(7700.0, 3, True)
        self.trip_booked_dest.booked_destinations_paid_amounts = {
            "Bulgaria": 3*500*0.9
        }

    def test_correct_init(self):
        self.assertEqual(6300.0, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(False, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_init_with_less_than_one_traveler_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_with_less_than_two_travelers(self):
        self.test = Trip(5000, 1, True)
        self.assertEqual(False, self.test.is_family)

    def test_book_a_trip_with_invalid_destination(self):
        self.assertEqual(
            'This destination is not in our offers, please choose a new one!',
            self.trip.book_a_trip("Kongo")
        )

    def test_book_a_trip_with_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!',
                         self.trip.book_a_trip('New Zealand')
                         )
        self.assertEqual('Your budget is not enough!',
                         self.trip_booked_dest.book_a_trip('New Zealand'))

    def test_book_a_trip_successfully_appends_and_reduce_budget(self):
        destination = "Bulgaria"
        expected_result = (f'Successfully booked destination {destination}! '
                           f'Your budget left is {(self.trip.budget - 1000):.2f}')

        self.assertEqual(expected_result, self.trip.book_a_trip(destination))

    def test_booking_status_with_NO_bookings(self):
        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}',
                         self.trip.booking_status()
                         )

    def test_booking_status__one_booking(self) :
        t = Trip(1000, 1, False)
        t.book_a_trip('Bulgaria')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 500.0})
        res = t.booking_status()
        self.assertEqual(res, """Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 500.00""")


if __name__ == "__main__":
    main()
