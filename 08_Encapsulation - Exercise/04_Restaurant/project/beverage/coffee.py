from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    PRICE = 3.5
    MILLILITERS = 50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
