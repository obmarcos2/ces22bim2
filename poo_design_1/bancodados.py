from cliente import Cliente
from interfaces import Produto
from autor import Autor


# este banco de dados tem pesquisa de livro por autor. Poderiamos usar uma interface
# para generalizar os tipos de busca dado a classe de produto. Caso vendesse a classe
# canetas, poderiamos usar uma busca por cor - ou marca - de caneta.
class Bancodados:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.autores = []

    def add_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def add_produto(self, produto: Produto):
        self.produtos.append(produto)

    def add_autor(self, autor: Autor):
        self.autores.append(autor)

    def busca_cliente(self, nome: str) -> bool:
        for c in self.clientes:
            if c.get_nome() == nome:
                return True
        return False

    def busca_produto(self, string: str):         #cada produto tem um nome de referencia
        print("Busca de produto em "+ string)
        for c in self.produtos:                   #para o livro, é o autor. essa busca enumera todas
            if c.parametro_de_busca() == string:  #as instancias que contem essa referencia
                print(c)