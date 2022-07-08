
class Autor:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.titulos = []

    def adic_livro(self, titulo):
        self.titulos.append(titulo)

    def get_nome(self):
        return self.nome