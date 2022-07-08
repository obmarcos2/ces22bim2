from abc import ABC, abstractmethod


class Produto(ABC):
    @abstractmethod
    def preco_venda(self) -> float:
        pass

    @abstractmethod
    def preco_compra(self) -> float:
        pass

    @abstractmethod
    def taxa_de_produto(self) -> float:
        pass

    @abstractmethod
    def parametro_de_busca(self):
        pass


class ImpostoLivro(ABC):
    @abstractmethod
    def calc_imposto(self) -> float:
        pass

    @abstractmethod
    def get_genero(self):
        pass

    @abstractmethod
    def get_compra(self):
        pass

    @abstractmethod
    def get_venda(self):
        pass
