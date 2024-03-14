from project.animal import Animal


class Lion(Animal):
    MONEY_TO_CARE = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.MONEY_TO_CARE)
