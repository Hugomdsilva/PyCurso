# Oque é visibilidade em um Objeto?
"""
 a visibilidade pode ser modificada com 3 coisas

 +  publico
           a classe atual e todas as outras classes tem acesso

 - privado
           somente a classe atual tem acesso

 # protegido
           a classe atual e todas as suas sub-classes tem acesso
"""


class Caneta1:
    def __init__(self, modelo='', cor='', ponta=0.0, carga=0, tampada=False):
        self.cor = cor
        self.modelo = modelo
        self.__tampada = tampada
        self.__carga = carga
        self.__ponta = ponta

    def rabiscar(self):
        if self.__tampada:
            print('Erro!! , nao posso rabiscar')
        else:
            print('Estou rabiscando')

    def __escrever(self):
        if self.__tampada:
            print('Erro!! , nao posso escrever')
        else:
            etc = input('escreva:')
            print(etc)

    def tampar(self):
        self.__tampada = True

    def destampar(self):
        self.__tampada = False

    def status(self):
        todo = [self.modelo, self.cor, self.__ponta, self.__carga, self.__tampada]
        print('Modelo =', todo[0])
        print('Uma caneta =', todo[1])
        print('Ponta =', todo[2])
        print('Carga =', todo[3])
        print('Está tampada? =', todo[4])


c1 = Caneta1()
c1.modelo = 'Bic cristal'
c1.cor = 'vermelha'
print(c1.cor)
c1.tampar() # modifiquei o tampada com o metodo tampar
c1.status()
# c1.ponta nao pode ser acessado pois está privado
# c1.__escrever() acontece o mesmo pois está privado