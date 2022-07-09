from abc import ABC, abstractmethod


# abstracao de motor, via interface
class IntMotor(ABC):
    @abstractmethod
    def get_potencia(self):
        pass

    @abstractmethod
    def get_vel(self):
        pass

    @abstractmethod
    def set_vel(self, velocidade: float):
        pass


# seguem as classes implementadas com tal interface
class MotorEletrico(IntMotor):
    def __init__(self, potencia, velocidade=0):
        self.potencia = potencia
        self.velocidade = velocidade

    def get_potencia(self):
        return self.potencia

    def get_vel(self):
        return self.velocidade

    def set_vel(self, velocidade):
        self.velocidade = velocidade


class MotorHibrido(IntMotor):
    def __init__(self, potencia, velocidade=0):
        self.potencia = potencia
        self.velocidade = velocidade

    def get_potencia(self):
        return self.potencia

    def get_vel(self):
        return self.velocidade

    def set_vel(self, velocidade):
        self.velocidade = velocidade


class MotorCombustao(IntMotor):
    def __init__(self, potencia, velocidade=0):
        self.potencia = potencia
        self.velocidade = velocidade

    def get_potencia(self):
        return self.potencia

    def get_vel(self):
        return self.velocidade

    def set_vel(self, velocidade):
        self.velocidade = velocidade
        return velocidade


# superclasse que o cliente vai manipular
class Veiculo:
    def __init__(self, implementation: IntMotor):
        self.motor = implementation

    def acelerar(self):
        a = self.motor.get_vel()
        acc = self.motor.get_potencia() * 0.1
        self.motor.set_vel(a + acc)

    def deacelerar(self):
        a = self.motor.get_vel()
        acc = -self.motor.get_potencia() * 0.1
        self.motor.set_vel(a + acc)


# alguns exemplos implementados
class Carro(Veiculo):
    def __init__(self, implementation, tipo_carro):
        super().__init__(implementation)
        self.tipo = tipo_carro

    @staticmethod
    def buzinar_carro():
        print('carro buzinou')


class Caminhao(Veiculo):
    def __init__(self, implementation, qte_eixo):
        super().__init__(implementation)
        self.qte_eixo = qte_eixo

    @staticmethod
    def buzinar_caminhao():
        print('caminhao buzinou')
