from typing import List
from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Food or Drink] = []

    def add(self, product: Food or Drink):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):

        searched_product = self.find(product_name)

        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)