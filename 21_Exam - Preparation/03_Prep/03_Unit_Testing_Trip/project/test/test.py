from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(1000,
                         10,
                         True
                         )

    def test_init_expect_success(self):
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual(10, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(self.trip.DESTINATION_PRICES_PER_PERSON,
                         {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500})

    def test_travelers_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.trip.travelers = 0
        self.assertEqual("At least one traveler is required!", str(ex.exception))

    def test_is_family_setter_expect_false(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_expect_destination_not_in_dict(self):
        expected_output = "This destination is not in our offers, please choose a new one!"
        result = self.trip.book_a_trip("USA")

        self.assertEqual(expected_output, result)

    def test_book_a_trip_expect_success_and_price_lower_is_family_is_true(self):
        expected_output = "Your budget is not enough!"
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(expected_output, result)

    def test_book_a_trip_with_money_expect_to_add_destination_to_list(self):
        self.trip.budget = 100_000
        expected_output = "Successfully booked destination Bulgaria! Your budget left is 95500.00"
        lower_budget_with = 4500

        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(expected_output, result)
        self.assertEqual(95_500, self.trip.budget)
        self.assertEqual({"Bulgaria": 4500}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_money_expect_to_add_destination_to_list_when_is_family_is_false(self):
        self.trip.budget = 10_000
        self.trip.travelers = 1
        self.trip.is_family = False
        expected_output = "Successfully booked destination New Zealand! Your budget left is 2500.00"
        lower_budget_with = 7500

        result = self.trip.book_a_trip("New Zealand")

        self.assertEqual(expected_output, result)
        self.assertEqual(2500, self.trip.budget)
        self.assertEqual({"New Zealand": 7500}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status_with_no_booked_destinations(self):
        expected_output = "No bookings yet. Budget: 1000.00"
        result = self.trip.booking_status()

        self.assertEqual(expected_output, result)

    def test_booking_status_with_booked_destinations_expected_sorted_dict(self):
        self.trip.budget = 1_000_000_000

        self.trip.book_a_trip("Australia")
        self.trip.book_a_trip("New Zealand")
        self.trip.book_a_trip("Brazil")
        self.trip.book_a_trip("Bulgaria")

        expected_output = f"Booked Destination: Australia\n" \
                          f"Paid Amount: 51300.00\n"
        expected_output += f"Booked Destination: Brazil\n" \
                           f"Paid Amount: 55800.00\n"
        expected_output += f"Booked Destination: Bulgaria\n" \
                           f"Paid Amount: 4500.00\n"
        expected_output += f"Booked Destination: New Zealand\n" \
                           f"Paid Amount: 67500.00\n"
        expected_output += f"Number of Travelers: 10\n" \
                           f"Budget Left: 999820900.00"

        result = self.trip.booking_status()

        self.assertEqual(expected_output, result)


if __name__ == "__main__":
    main()
