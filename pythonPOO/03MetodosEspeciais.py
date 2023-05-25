#Oque são Métodos especiais
"""
Metodo acessor (getters) metodo para acessar determinado atributo que nao tem acesso sem o metodo
"""

"""
Metodo modificadores (setters) metodo para modificar determinado atributo sem acesso direto
"""

class Caneta:
    def __init__(self, modelo='', ponta=0.0):
        self.__ponta = ponta
        self.__modelo = modelo

    def getmodelo(self):
        return self.__modelo

    def setmodelo(self, modelo):
        self.__modelo = modelo

    def getponta(self):
        return self.__ponta

    def setponta(self, ponta):
        self.__ponta = ponta

    def status(self):
        print('Sobre a Caneta:')
        print('Modelo:', self.getmodelo())
        print('Ponta:', self.getponta())


c1 = Caneta()
c1.setmodelo('BIC')
c1.setponta(0.5)
c1.status()