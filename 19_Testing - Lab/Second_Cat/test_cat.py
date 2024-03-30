from unittest import TestCase, main
# from Second_Cat.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat(
            "Fredy",
        )

    def test_init_if_its_correct_expect_success(self):
        self.assertEqual("Fredy", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_when_cat_is_already_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_eat_when_cat_is_not_fed_expect_success(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_when_cat_is_still_hungry_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_speed_when_cat_has_already_eaten(self):
        self.cat.eat()

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)
        self.assertTrue(self.cat.fed)


if __name__ == "__main__":
    main()