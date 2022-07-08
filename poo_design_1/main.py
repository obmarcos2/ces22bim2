from cliente import Cliente
from autor import Autor
from livro import Livro, TaxalivroRomance
from bancodados import Bancodados

aut = Autor("lisa", "@ga")
aut2 = Autor("joao", "@hotmal")
Tax = TaxalivroRomance(30.5, 45)
A = Livro("livro 1", Tax, aut, "edit1", 4)
aut.adic_livro("livro 1")
B = Livro("livro2", Tax, aut2, "editora 2", 1)
aut2.adic_livro("livro2")
print(B)

client = Cliente("carlos", "abc@ga")
C = client.get_carrinho()
C.add_produto(A)
C.remove_produto(B)
C.add_produto(B)
C.listar_produtos()
C.remove_produto(A)
C.listar_produtos()

D = Bancodados()
D.add_produto(B)
D.add_produto(A)
D.add_autor(aut)
D.add_autor(aut2)
D.add_cliente(client)

D.busca_produto("joao")

