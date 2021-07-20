from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return f'Sou o principe {self.__nome}, o que esta procurando aqui insolente!'
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return 'Sou o principe dos saiyajins não devo boas vindas a voce'

    def despedida(self):
        return 'Adeus miseravel!'