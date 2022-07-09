from interfaces import *

m1 = MotorCombustao(120)
m2 = MotorEletrico(150)
# criacao do objeto de interface veiculo com
# agregacao de motores distintos
veic = Carro(m1, "sedan")
veic.buzinar_carro()

veic2 = Carro(m2, "hatch")
veic2.buzinar_carro()
veic2.acelerar()
print(m2.get_vel())
print(m1.get_vel())
