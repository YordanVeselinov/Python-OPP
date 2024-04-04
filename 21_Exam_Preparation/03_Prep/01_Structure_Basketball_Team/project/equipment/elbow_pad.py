from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    INITIAL_PROTECTION = 90
    INITIAL_PRICE = 25.0
    TYPE_ = "ElbowPad"

    def __init__(self):
        super().__init__(self.INITIAL_PROTECTION, self.INITIAL_PRICE)

    def increase_price(self):
        self.price *= 1.10