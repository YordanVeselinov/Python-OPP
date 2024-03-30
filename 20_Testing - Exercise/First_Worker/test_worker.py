from unittest import TestCase, main
from First_Worker.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Test", 1500, 10)

    def test_correct_init(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1500, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_zero_or_below_zero_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        self.worker.energy = -100

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_positive_energy_expect_success(self):
        self.worker.work()

        self.assertEqual(9, self.worker.energy)
        self.assertEqual(1500, self.worker.money)

    def test_rest_expect_energy_to_go_up_with_one(self):
        self.worker.rest()

        self.assertEqual(11, self.worker.energy)

    def test_get_info_expect_string_showing_details_of_the_worker(self):
        self.worker.work()

        expected_string = f"Test has saved 1500 money."
        result = self.worker.get_info()

        self.assertEqual(expected_string, result)


if __name__ == "__main__":
    main()
