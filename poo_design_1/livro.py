from autor import Autor
from interfaces import Produto, ImpostoLivro


class Livro(Produto):
    def __init__(self, titulo, imposto: ImpostoLivro, autor: Autor, editora, edicao):
        self.titulo = titulo
        self.genero = imposto.get_genero()
        self.imposto = imposto
        self.autor = autor
        self.editora = editora
        self.edicao = edicao
        self.venda = imposto.get_venda()
        self.compra = imposto.get_compra()

    def __str__(self):
        return 'Titulo: ' + self.titulo + '\nAutor: ' + self.autor.get_nome() + '\nGenero' \
               + self.genero + "\nPreco em reais " + str(self.venda)

    def obter_titulo(self):
        print(self.titulo)
        return self.titulo

    def preco_venda(self):
        print(self.venda)
        return self.venda

    def preco_compra(self):
        print(self.compra)
        return self.compra

    def taxa_de_produto(self):
        return self.imposto.calc_imposto()

    def parametro_de_busca(self):
        return self.autor.get_nome()


class TaxalivroRomance(ImpostoLivro):
    def __init__(self, compra, venda):
        self.genero = "Romance"
        self.compra = compra
        self.venda = venda

    def get_genero(self):
        return self.genero

#    @staticmethod
    def calc_imposto(self) -> float:
        return (self.venda - self.compra)*0.3 #para outros generos este metodo muda

    def get_compra(self):
        return self.compra

    def get_venda(self):
        return self.venda

