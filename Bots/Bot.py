# implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(self, nome: str):
        self.nome = nome
        self.comandos = {'1': 'Bom dia', '2': 'Qual seu nome?', '3': 'Quero um conselho', '4': 'Adeus'}

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def mostra_comandos(self):
        for key in self.comandos:
            print(key, self.comandos[key])

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass