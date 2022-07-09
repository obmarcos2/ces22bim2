from abc import ABC, abstractmethod


class DoceBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_sabor(self, sabor):
        pass

    @abstractmethod
    def set_peso(self, peso):
        pass

    @abstractmethod
    def set_tipo(self, tipo):
        pass


class BoloBuilder(DoceBuilder):
    def __init__(self):
        self.bolo = None

    def reset(self):
        self.bolo = Bolo()

    def set_sabor(self, sabor):
        self.bolo.sabor = sabor

    def set_peso(self, peso):
        self.bolo.peso = peso

    def set_tipo(self, tipo):
        self.bolo.tipo = tipo

    def get_resultado(self):
        return self.bolo


class Bolo:
    def __init__(self, sabor=None, peso=0, tipo=None):
        self.sabor = sabor
        self.peso = peso
        self.tipo = tipo

#criar classe torta doce, chocolate, etc para adicionar
#na interface