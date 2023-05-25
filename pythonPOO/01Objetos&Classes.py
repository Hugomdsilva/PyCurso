# Oque é um objeto?
"""
" Uma coisa material ou abstrata que pode ser percebida
pelos sentidos e descrita por meio das suas caracteristicas
comportamento e estado atual "

"""

# Oque é uma Classe?
"""
" Define os atributos e metodos comuns que serão compartilhados por um objeto "
"""


class Caneta:
    def __init__(self, modelo='', cor='', ponta=0.0, carga=0, tampada=False):
        self.tampada = tampada
        self.carga = carga
        self.cor = cor
        self.modelo = modelo
        self.ponta = ponta

    def rabiscar(self):
        if self.tampada:
            print('Erro!! , nao posso rabiscar')
        else:
            print('Estou rabiscando')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def status(self):
        todo = [self.modelo, self.cor, self.ponta, self.carga, self.tampada]
        print('Modelo =', todo[0])
        print('Uma caneta =', todo[1])
        print('Ponta =', todo[2])
        print('Carga =', todo[3])
        print('Está tampada? =', todo[4])


c1 = Caneta()
c1.modelo = 'BIC'
c1.cor = 'azul'
c1.ponta = 0.5
c1.carga = 10
c1.tampada = False

c1.rabiscar()

c2 = Caneta('Montblac', 'Preta', 1, 9, True)
c2.destampar()
c2.rabiscar()

c1.status()
c2.status()