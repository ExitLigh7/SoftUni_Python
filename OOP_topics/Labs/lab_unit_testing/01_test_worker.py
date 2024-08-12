class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Testony", 1000, 100)

    def test_correct_init(self):
        self.assertEqual("Testony", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_zero_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_negative_energy_raises_exception(self):
        self.worker.energy = -10

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_enough_energy_increases_money_decrease_energy(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_rest_increases_energy(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        expected = f'Testony has saved 0 money.'
        self.assertEqual(expected, self.worker.get_info())


if __name__ == "__main__":
    main()
