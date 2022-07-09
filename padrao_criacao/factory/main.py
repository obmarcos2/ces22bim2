from cliente import *
from interfaces import *

F = Factory2()
A = Cliente(F)
s = A.get_product()

print(s.tipo())