from carrinho import Carrinho


class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.carrinho = Carrinho()

    def get_nome(self):
        return self.nome

    def get_carrinho(self):
        return self.carrinho
