from interfaces import *
from typing import Type


class Cliente:
    def __init__(self, factory: Type[AbstractFactory]):
        self.factory = factory
        self.product1 = self.get_product()

    def get_product(self):
        return self.factory.create1()
