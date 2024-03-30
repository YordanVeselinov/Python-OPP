from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(80, 250)

    def test_init_expect_success(self):
        self.assertEqual(80, self.vehicle.capacity)
        self.assertEqual(80, self.vehicle.fuel)
        self.assertEqual(250, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_when_fuel_is_less_than_fuel_needed_raised_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_when_fuel_is_more_than_fuel_needed_expect_success(self):
        self.vehicle.drive(10)

        self.assertEqual(67.5, self.vehicle.fuel)

    def test_refuel_fuel_is_greater_than_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_fuel_is_less_than_capacity_expect_success(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(10)

        self.assertEqual(20, self.vehicle.fuel)

    def test_str_method_returns_the_correct_string(self):
        expected_string = "The vehicle has 250 " \
                          "horse power with 80 " \
                          "fuel left and 1.25 " \
                           "fuel consumption"

        self.assertEqual(expected_string, str(self.vehicle))


if __name__ == "__main__":
    main()
