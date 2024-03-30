from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("John", 10, 1500, 100)
        self.enemy = Hero("Mike", 10, 1500, 100)

    def test_battle_when_hero_and_enemy_has_same_name_raises_exception(self):
        self.enemy.username = "John"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_has_zero_or_less_health_raises_exception(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest"
                         , str(ex.exception))

        self.hero.health = -1000

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest"
                         , str(ex.exception))

    def test_battle_when_enemy_has_zero_or_less_health_raises_exception(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Mike. He needs to rest"
                         , str(ex.exception))

        self.enemy.health = -1000

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Mike. He needs to rest"
                         , str(ex.exception))

    def test_battle_when_both_health_becomes_zero_or_less_expects_draw(self):
        self.hero.health = 10
        self.enemy.health = 10
        expected_result = "Draw"

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_result, result)
        self.assertEqual(-990, self.hero.health)
        self.assertEqual(-990, self.enemy.health)

    def test_battle_when_hero_wins_expect_stats_up_and_success(self):
        self.enemy.health = 10
        expected_result = "You win"

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_result, result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(505, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_when_enemy_wins_expect_stats_up_and_success(self):
        self.hero.health = 10
        expected_result = "You lose"

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_result, result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(505, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str_on_hero(self):
        expected_string = f"Hero John: 10 lvl\n" \
                          f"Health: 1500\n" \
                          f"Damage: 100\n"

        self.assertEqual(expected_string, str(self.hero))


if __name__ == "__main__":
    main()
