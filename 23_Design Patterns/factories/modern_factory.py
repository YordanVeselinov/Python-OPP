from factories.abstract_furntiture_factory import AbstractFactory
from factories.furnitures.sofa import Sofa
from factories.furnitures.chair import Chair
from factories.furnitures.table import Table


class ModernFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa("Modern")

    def create_chair(self):
        return Chair("Modern")

    def create_table(self):
        return Table("Modern")