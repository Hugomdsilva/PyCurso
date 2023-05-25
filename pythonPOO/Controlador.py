#<<Controlador>>
from abc import ABC, abstractmethod
class Controlador(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @abstractmethod
    def abrirMenu(self):
        pass
    @abstractmethod
    def fecharMenu(self):
        pass
    @abstractmethod
    def maisVolume(self):
        pass
    @abstractmethod
    def menosVolume(self):
        pass
    @abstractmethod
    def ligarMudo(self):
        pass
    @abstractmethod
    def desligarMudo(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
