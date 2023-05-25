import random


class ContaBanco:
    def __init__(self, numConta=0000, tipo='', dono='', saldo=0.0, status=False):
        self.numConta = numConta
        self.tipo = tipo
        self.__dono = dono
        self.__saldo = saldo
        self.__status = status

    def __verificador(self):
        if not self.__status:
            print('A conta está fechada ou nunca foi aberta')
            exit()

    def abrirCC(self):
        self.numConta = random.randint(0000, 9999)
        self.tipo = 'Corrente'
        self.__status = True
        self.__saldo = 50

    def abrirCP(self):
        self.numConta = random.randint(0000, 9999)
        self.tipo = 'Poupança'
        self.__status = True
        self.__saldo = 150

    def sacar(self, saldo):
        self.__verificador()
        if saldo > self.__saldo:
            print('Não é possivel sacar mais doque voce tem na conta seu saldo é de {:.2f}'.format(self.__saldo))
        else:
            self.__saldo -= saldo
            print('Voce sacou {:.2f}R$ seu saldo atual é de {:.2f}R$'.format(saldo, self.__saldo))

    def depositar(self, saldo=0):
        self.__verificador()
        self.__saldo += saldo
        print('Voce depositou {:.2f}R$ seu saldo atual é de {:.2f}R$'.format(saldo, self.__saldo))

    def pagarMensal(self):
        self.__verificador()
        if self.tipo == 'Corrente':
            self.__saldo -= 12
            print('Voce pagou a mensalidade com sucesso foi debitado 12R$ de sua conta')
        else:
            self.__saldo -= 20
            print('Voce pagou a mensalidade com sucesso foi debitado 20R$ de sua conta')

    def fecharConta(self):
        self.__verificador()
        if self.__saldo > 0:
            a = str(input(
                'Não é possivel fechar a conta com saldo positivo deseja sacar seu dinheiro atual? S/N'.format(
                    self.__saldo)))
            if a == 'S' or 's':
                self.sacar(self.__saldo)
            else:
                print('O processo de fechar conta foi cancelado')

        elif self.__saldo < 0:
            d = abs(self.__saldo)
            a = input(
                'Não é possivel fechar a conta com saldo negativo para isso deposite o valor de {:.2f}R$'.format(d))
            'Deseja depositar S/N:'
            if a == 'S' or 's':
                self.depositar(d)

        if self.__saldo == 0:
            self.__status = False
            print('Conta fechada com sucesso')


