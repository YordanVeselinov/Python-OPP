from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.animal = Mammal(
            "Test",
            "Tiger",
            "Roar"
        )

    def test_init_expect_success(self):
        self.assertEqual("Test", self.animal.name)
        self.assertEqual('Tiger', self.animal.type)
        self.assertEqual("Roar", self.animal.sound)
        self.assertEqual("animals", self.animal.get_kingdom())

    def test_make_sound_expect_success(self):
        expected_return = "Test makes Roar"

        result = self.animal.make_sound()

        self.assertEqual(expected_return, result)

    def test_info_expect_success(self):
        expected_return = "Test is of type Tiger"

        result = self.animal.info()

        self.assertEqual(expected_return, result)



if __name__ == "__main__":
    main()
