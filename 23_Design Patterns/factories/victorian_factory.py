from factories.abstract_furntiture_factory import AbstractFactory
from factories.furnitures.sofa import Sofa
from factories.furnitures.chair import Chair
from factories.furnitures.table import Table


class VictorianFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa("Victorian")

    def create_chair(self):
        return Chair("Victorian")

    def create_table(self):
        return Table("Victorian")