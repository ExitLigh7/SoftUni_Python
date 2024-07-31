from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Ivan", 10)
        self.driver.available_cargos = {"Plovdiv": 80}

    def test_correct_init(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({"Plovdiv": 80}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_with_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_already_added_offer(self):
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Plovdiv", 80)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_adds_successfully(self):
        cargo_miles, cargo_location = 100, "Sofia"
        expected = f"Cargo for {cargo_miles} to {cargo_location} was added as an offer."

        self.assertEqual(expected, self.driver.add_cargo_offer(cargo_location, cargo_miles))
        self.assertEqual({"Plovdiv": 80, "Sofia": 100} , self.driver.available_cargos)

    def test_drive_best_cargo_offer_correctly_chooses_no_activities(self):
        self.driver.add_cargo_offer("Sofia", 100)

        expected = f"{self.driver.name} is driving 100 to Sofia."
        self.assertEqual(expected, self.driver.drive_best_cargo_offer())
        self.assertEqual(1000, self.driver.earned_money)
        self.assertEqual(100, self.driver.miles)

    def test_drive_best_cargo_offer_with_no_offer_returns_error_msg(self):
        self.driver.available_cargos = {}
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_check_for_activities_1000_miles_should_eat_4_times_and_sleep_once(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1000)
        self.assertEqual(875, self.driver.earned_money)

    def test_check_for_activities_1500_miles_eat_6_times_sleep_and_pump_gas_once(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1500)
        self.assertEqual(335, self.driver.earned_money)

    def test_check_repair_truck(self):
        self.driver.earned_money = 10_000
        self.driver.repair_truck(10000)
        self.assertEqual(2500, self.driver.earned_money)

    def test__repr__returns_correct_string(self):
        expected = f"{self.driver.name} has {self.driver.miles} miles behind his back."
        self.assertEqual(expected, self.driver.__repr__())

    def test_bankrupt(self) :
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer ( "California", 2000 )

        with self.assertRaises ( ValueError ) as ve :
            self.driver.drive_best_cargo_offer ()

        self.assertEqual ( str ( ve.exception ), f"{self.driver.name} went bankrupt." )
    

if __name__ == "__main__":
    main()
