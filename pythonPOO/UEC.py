import random


class Lutador:
    def __init__(self, nome='', nacionalidade='', idade=0, altura=0.0, peso=0.0, vitorias=0, derrotas=0,
                 empates=0, categoria=''):
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self._categoria = categoria
        self._vitorias = vitorias
        self._derrotas = derrotas
        self._empates = empates
        self._setPeso(peso)

    def _getNome(self):
        return self._nome

    def _getNacionalidade(self):
        return self._nacionalidade

    def _getIdade(self):
        return self._idade

    def _getAltura(self):
        return self._altura

    def _getPeso(self):
        return self._peso

    def getCategoria(self):
        return self._categoria

    def _getVitorias(self):
        return self._vitorias

    def _getDerrotas(self):
        return self._derrotas

    def _getEmpates(self):
        return self._empates

    def _setNome(self, value):
        self._nome = value

    def _setNacionalidade(self, value):
        self._nacionalidade = value

    def _setIdade(self, value):
        self._idade = value

    def _setAltura(self, value):
        self._altura = value

    def _setCategoria(self, value):
        self._categoria = value

    def _setPeso(self, value):
        self._peso = value
        if self._peso < 52.2:
            self._setCategoria('Inválido')
        elif self._peso <= 70.3:
            self._setCategoria('Leve')
        elif self._peso <= 83.9:
            self._setCategoria('Médio')
        elif self._peso < 120.2:
            self._setCategoria('Pesado')
        else:
            self._setCategoria('Inválido')

    def _setVitorias(self, value):
        self._vitorias = value

    def _setDerrotas(self, value):
        self._derrotas = value

    def _setEmpates(self, value):
        self._empates = value

    def ganharLuta(self):
        self._setVitorias(self._getVitorias() + 1)

    def perderLuta(self):
        self._setDerrotas(self._getDerrotas() + 1)

    def empatarLuta(self):
        self._setEmpates(self._getEmpates() + 1)

    def apresentar(self):
        print('Lutador: ', self._getNome())
        print('Origem: ', self._getNacionalidade())
        print('Com: ',self._getIdade(), ' anos')
        print('Tendo: ',self._getAltura(), 'm de altura')
        print('Pesando: ', self._getPeso(), 'Kg')
        print('Ganhou: ', self._getVitorias())
        print('Perdeu: ', self._getDerrotas())
        print('Empatou: ', self._empates)

    def status(self):
        print(self._getNome())
        print('é um peso ', self.getCategoria())
        print(self._getVitorias(), 'Vitorias')
        print(self._getDerrotas(), 'Derrotas')
        print(self._getEmpates(), 'Empates')


class Luta:
    def __init__(self, desafiado=Lutador, desafiante=Lutador, rounds=None, aprovada=None):
        self._desafiado = Lutador
        self._desafiante = Lutador
        self._rounds = rounds
        self._aprovada = aprovada

    def setDesafiado(self, Lutador):
        self._desafiado = Lutador

    def setDesafiante(self, Lutador):
        self._desafiante = Lutador

    def marcarLuta(self, L1, L2):
        if L1.getCategoria() == L2.getCategoria() and L1 != L2:
            self.__aprovada = True
            self.setDesafiante(L1)
            self.setDesafiado(L2)
        else:
            self.__aprovada = False
            self.__desafiado = None
            self.__desafiante = None

    def lutar(self):
        if self.__aprovada:
            print('DESAFIADO: \n')
            self._desafiado.apresentar()
            print('DESAFIANTE: \n')
            self._desafiante.apresentar()
            vencedor = random.randint(0, 2) 
            match vencedor:
                case 0:
                    print('EMPATE')
                    self._desafiante.empatarLuta()
                    self._desafiado.empatarLuta()
                case 1:
                    print('DESAFIANTE GANHOU')
                    self._desafiante.ganharLuta()
                    self._desafiado.perderLuta()
                case 2:
                    print('DESAFIADO GANHOU')
                    self._desafiante.perderLuta()
                    self._desafiado.ganharLuta()
        else:
            print('Luta nao pode acontecer')


L = [0, 1, 2, 3, 4, 5]
L[0] = Lutador('Pretty Boy', 'França', 31, 1.75, 68.9, 11, 3, 1)
L[1] = Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 14, 2, 3)
L[2] = Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 12, 2, 1)
L[3] = Lutador('Dead code', 'Austrália', 28, 1.93, 81.6, 13, 0, 2)
L[4] = Lutador('UFOCobol', 'Brasil', 37, 1.70, 119.3, 5, 4, 3)
L[5] = Lutador('Nerdaart', 'EUA', 30, 1.81, 105.7, 12, 2, 4)

Box = Luta()

Box.marcarLuta(L[0], L[1])
Box.lutar()
