from interfaces import Produto
from typing import Type

class Carrinho:
    def __init__(self):
        self.produto = []

    def add_produto(self, produto: Type[Produto]):
        self.produto.append(produto)
        print("Produto adicionado")

    def remove_produto(self, produto: Type[Produto]):
        for c in self.produto:
            if c == produto:
                self.produto.remove(c)
                print("Produto Removido")
                return
            else:
                continue
        print("Produto não existente")

    def listar_produtos(self):
        print('Produtos no carrinho:')
        for c in self.produto:
            print(c)
            print('\n')

    def limpar_carrinho(self):
        self.produto = []