from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    INITIAL_PROTECTION = 120
    INITIAL_PRICE = 15.0
    TYPE_ = "KneePad"

    def __init__(self):
        super().__init__(self.INITIAL_PROTECTION, self.INITIAL_PRICE)

    def increase_price(self):
        self.price *= 1.20
