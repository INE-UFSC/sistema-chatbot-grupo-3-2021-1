from Bots.Bot import Bot


class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome

    # nao esquecer o decorator
    def nome(self):
         return self.__nome

    # nao esquecer o decorator
    def nome(nome):
        pass

    def apresentacao(self):
        return "Oiiii. Meu nome é {}. :)".format(self.__nome)

    def mostra_comandos(self):
        pass

    def executa_comando(self, cmd):
        pass

    def boas_vindas(self):
        return "Seja bem vindesss :)"

    def despedida(self):
        return "Adeusinho. Vou sentir sua falta :)"
