from abc import ABC, abstractmethod


class Bolo_choc(ABC):
    @abstractmethod
    def tipo(self) -> str:
        pass


class Bolo_mand(ABC):
    @abstractmethod
    def tipo(self) -> str:
        pass


class Bolo_cen(ABC):
    @abstractmethod
    def tipo(self) -> str:
        pass


class Bolo_choc_aniv(Bolo_choc):
    def tipo(self) -> str:
        return "aniversario"


class Bolo_choc_cas(Bolo_choc):
    def tipo(self) -> str:
        return "casamento"


class Bolo_choc_inf(Bolo_choc):
    def tipo(self) -> str:
        return "informal"


class Bolo_mand_aniv(Bolo_mand):
    def tipo(self) -> str:
        return "aniversario"


class Bolo_mand_cas(Bolo_mand):
    def tipo(self) -> str:
        return "casamento"


class Bolo_mand_inf(Bolo_mand):
    def tipo(self) -> str:
        return "informal"


class Bolo_cen_aniv(Bolo_cen):
    def tipo(self) -> str:
        return "aniversario"


class Bolo_cen_cas(Bolo_cen):
    def tipo(self) -> str:
        return "casamento"


class Bolo_cen_inf(Bolo_cen):
    def tipo(self) -> str:
        return "informal"


# constroi um conjunto de criacoes de todos as interfaces de bolo para uma
# dada especificacao
class AbstractFactory(ABC):
    @abstractmethod
    def create1(self) -> Bolo_choc:
        pass

    @abstractmethod
    def create2(self) -> Bolo_mand:
        pass

    @abstractmethod
    def create3(self) -> Bolo_cen:
        pass


class Factory1(AbstractFactory):
    def create1(self) -> Bolo_choc:
        return Bolo_choc_aniv()

    def create2(self) -> Bolo_mand:
        return Bolo_mand_aniv()

    def create3(self) -> Bolo_cen:
        return Bolo_cen_aniv()


class Factory2(AbstractFactory):
    def create1(self) -> Bolo_choc:
        return Bolo_choc_cas()

    def create2(self) -> Bolo_mand:
        return Bolo_mand_cas()

    def create3(self) -> Bolo_cen:
        return Bolo_cen_cas()


class Factory3(AbstractFactory):
    def create1(self) -> Bolo_choc:
        return Bolo_choc_inf()

    def create2(self) -> Bolo_mand:
        return Bolo_mand_inf()

    def create3(self) -> Bolo_cen:
        return Bolo_cen_inf()
