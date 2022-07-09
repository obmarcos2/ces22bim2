from interfaces import *


class Diretor:
    def __init__(self, doce: DoceBuilder):
        self.builder = doce

    def make_doce(self, sabor, peso, tipo):
        self.builder.set_peso(peso)
        self.builder.set_tipo(tipo)
        self.builder.set_sabor(sabor)
