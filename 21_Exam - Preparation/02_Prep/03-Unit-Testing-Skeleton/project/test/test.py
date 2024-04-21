from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.stations = RailwayStation("Sofia")

    def test_init_expect_success(self):
        self.assertEqual("Sofia", self.stations.name)
        self.assertEqual(deque(), self.stations.arrival_trains)
        self.assertEqual(deque(), self.stations.departure_trains)

    def test_name_with_less_than_or_equal_of_three_raised_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.stations.name = "two"

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.stations.name = "o"

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board_expect_success(self):
        self.stations.new_arrival_on_board("Some text")
        self.assertEqual(deque(["Some text"]), self.stations.arrival_trains)

    def test_train_has_arrived_expect_success_train_need_to_wait(self):
        self.assertEqual(0, len(self.stations.departure_trains))
        self.assertEqual(0, len(self.stations.arrival_trains))
        expected_output = "There are other trains to arrive before Some Text1234."

        self.stations.new_arrival_on_board("Some Text")

        self.assertEqual(0, len(self.stations.departure_trains))
        self.assertEqual(1, len(self.stations.arrival_trains))

        result = self.stations.train_has_arrived("Some Text1234")

        self.assertEqual(expected_output, result)

        self.assertEqual(0, len(self.stations.departure_trains))
        self.assertEqual(1, len(self.stations.arrival_trains))

    def test_train_has_arrived_expect_success_train_to_go_to_departure_trains(self):
        expected_output = f"Some Text is on the platform and will leave in 5 minutes."

        self.stations.new_arrival_on_board("Some Text")
        result = self.stations.train_has_arrived("Some Text")

        self.assertEqual(expected_output, result)

        self.assertEqual(1, len(self.stations.departure_trains))
        self.assertEqual(0, len(self.stations.arrival_trains))

    def test_train_has_left_expect_true(self):
        self.stations.new_arrival_on_board("Some Text")
        self.stations.train_has_arrived("Some Text")
        result = self.stations.train_has_left("Some Text")

        self.assertTrue(result)
        self.assertEqual(len(self.stations.departure_trains), 0)

    def test_train_has_left_expect_false(self):
        self.stations.new_arrival_on_board("Some Text")
        self.stations.train_has_arrived("Some Text")
        result = self.stations.train_has_left("Some Text,235221")

        self.assertFalse(result)


if __name__ == "__main__":
    main()
