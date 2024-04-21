from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar(
            "BMW",
            "sedan",
            100_000,
            100_000
        )
        self.car_diff = SecondHandCar(
            "BMW",
            "combi",
            100_000,
            100_000
        )

    def test_init_expect_success(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("sedan", self.car.car_type)
        self.assertEqual(100_000, self.car.mileage)
        self.assertEqual(100_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_expect_value_error(self):
        expected_output = "Price should be greater than 1.0!"

        with self.assertRaises(ValueError) as ex:
            self.car.price = 1

        self.assertEqual(expected_output, str(ex.exception))

    def test_mileage_setter_expect_value_error(self):
        expected_output = "Please, second-hand cars only! Mileage must be greater than 100!"

        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100

        self.assertEqual(expected_output, str(ex.exception))

    def test_set_promotional_price_expect_value_error(self):
        expected_output = "You are supposed to decrease the price!"

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(100_000)

        self.assertEqual(expected_output, str(ex.exception))

    def test_set_promotional_price_expect_success(self):
        expected_output = "The promotional price has been successfully set."
        result = self.car.set_promotional_price(10_000)

        self.assertEqual(expected_output, result)
        self.assertEqual(10_000, self.car.price)

    def test_need_repair_expect_repair_impossible(self):
        expected_output = "Repair is impossible!"

        result = self.car.need_repair(1_000_000, "suspension")

        self.assertEqual(expected_output, result)

    def test_need_repair_expect_to_increase_price(self):
        expected_output = "Price has been increased due to repair charges."

        result = self.car.need_repair(10_000, "suspension")

        self.assertEqual(expected_output, result)
        self.assertEqual(110_000, self.car.price)
        self.assertEqual(["suspension"], self.car.repairs)

    def test__gt__expect_car_cannot_be_compared(self):
        expected_output = "Cars cannot be compared. Type mismatch!"
        result = self.car > self.car_diff

        self.assertEqual(expected_output, result)

        result = self.car < self.car_diff

        self.assertEqual(expected_output, result)

    def test__gt__expect_true_or_false(self):
        self.car_diff.car_type = "sedan"

        result = self.car > self.car_diff

        self.assertFalse(result)

        self.car.price = 1_000_000

        result = self.car > self.car_diff

        self.assertTrue(result)

        result = self.car < self.car_diff

        self.assertFalse(result)

        self.car_diff.price = 1_000_000

        result = self.car < self.car_diff

        self.assertFalse(result)

    def test__str__should_return_formatted_string(self):
        expected_output = "Model BMW | Type sedan | Milage 100000km\nCurrent price: 100000.00 | Number of Repairs: 0"
        result = str(self.car)

        self.assertEqual(expected_output, result)


if __name__ == "__main__":
    main()
