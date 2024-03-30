from unittest import TestCase, main
# from Third_List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.list = IntegerList("Hello", 1, 3, 4, 5, 4.4)

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 3, 4, 5], self.list.get_data())

    def test_add_with_not_int_element_raised_value_error(self):
        expected_message = "Element is not Integer"

        with self.assertRaises(ValueError) as ve:
            self.list.add("Error")

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_with_int_expect_success(self):

        expected_list = [1, 3, 4, 5, 100]

        result = self.list.add(100)

        self.assertEqual(expected_list, result)

    def test_remove_index_with_invalid_index_raised_index_error(self):
        expected_message = "Index is out of range"

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(4)

        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(5)

        self.assertEqual(expected_message, str(ex.exception))

    def test_remove_index_with_valid_index_expect_success(self):
        expected_outcome = 1

        result = self.list.remove_index(0)

        self.assertEqual(expected_outcome, result)

    def test_get_with_index_out_of_the_list_raised_index_error(self):
        expected_message = "Index is out of range"

        with self.assertRaises(IndexError) as ex:
            self.list.get(4)

        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.list.get(5)

        self.assertEqual(expected_message, str(ex.exception))

    def test_get_with_valid_index_expect_success(self):
        expected_outcome = 1

        result = self.list.get(0)

        self.assertEqual(expected_outcome, result)

    def test_insert_with_invalid_index_raised_index_error(self):
        expected_message = "Index is out of range"

        with self.assertRaises(IndexError) as ex:
            self.list.insert(4, 1)

        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.list.insert(5, 1)

        self.assertEqual(expected_message, str(ex.exception))

    def test_insert_with_invalid_type_raised_value_error(self):
        expected_message = "Element is not Integer"

        with self.assertRaises(ValueError) as ex:
            self.list.insert(1, "ERROR!!!!")

        self.assertEqual(expected_message, str(ex.exception))

    def test_insert_with_valid_index_and_valid_type(self):
        expected_list = [100, 1, 3, 4, 5]

        self.list.insert(0, 100)

        self.assertEqual(self.list.get_data(), expected_list)

    def test_get_bigger_expect_success(self):
        expected_return = 100

        self.list.insert(1, 100)

        result = self.list.get_biggest()

        self.assertEqual(expected_return, result)

    def test_get_index_expect_success(self):
        expected_return = 3

        result = self.list.get_index(5)

        self.assertEqual(expected_return, result)







if __name__ == "__main__":
    main()
