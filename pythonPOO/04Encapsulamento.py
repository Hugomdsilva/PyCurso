# Oque é encapsulamento?
"""
Encapsulamento
Ocultar partes
independentes da
implementação,
permitindo construir
partes invisíveis ao
mundo exterior.

Interface
Lista de serviços
fornecidos por um
componente É o
contato com o
mundo exterior, que
define o que pode
ser feito com um
objeto dessa classe.
"""
from abc import ABC

from Controlador import Controlador


class ControleRemoto(Controlador, ABC):

    def __init__(self, volume=50, aux=50, ligado=False, tocando=False):
        self.__aux = aux
        self.__tocando = tocando
        self.__ligado = ligado
        self.__volume = volume

    def __getVolume(self) -> int:
        return self.__volume

    def __getLigado(self):
        return self.__ligado

    def __getTocando(self):
        return self.__tocando

    def __setVolume(self, variavel):
        self.__volume = variavel

    def __setLigado(self, variavel):
        self.__ligado = variavel

    def __setTocando(self, variavel):
        self.__tocando = variavel

    def ligar(self):
        self.__setLigado(True)

    def desligar(self):
        self.__setLigado(False)

    def fecharMenu(self):
        print('fechando menu')

    def maisVolume(self):
        V = self.__getVolume()
        Maisvolume = V = + 1
        if self.__getLigado():
            self.__setVolume(Maisvolume)
        else:
            print('Impossivel aumentar Volume')

    def menosVolume(self):
        V = self.__getVolume()
        Menosvolume = V - 1
        if self.__getLigado():
            self.__setVolume(Menosvolume)
        else:
            print('impossivel diminuir volume')

    def ligarMudo(self):
        self.__aux == self.__getVolume()
        if self.__getLigado() and self.__getVolume() > 0:
            self.__setVolume(0)

    def desligarMudo(self):
        if self.__getLigado() and self.__getVolume() == 0:
            self.__setVolume(self.__aux)

    def play(self):
        if self.__getLigado() and not self.__getTocando():
            self.__setTocando(True)

    def pause(self):
        if self.__getLigado() and self.__getTocando():
            self.__setTocando(False)

    def abrirMenu(self):
        print('-' * 10, 'MENU', '-' * 10)
        print('Está ligado?', self.__getLigado())
        print('Está tocando?', self.__getLigado())
        print('Volume: ', self.__getVolume())
        a = self.__getVolume()
        for i in range(a, 100, 10):
            print('| ', end='')
        print('\n')
        print('Está tocando?', self.__getTocando())


C = ControleRemoto()
C.ligar()
C.abrirMenu()