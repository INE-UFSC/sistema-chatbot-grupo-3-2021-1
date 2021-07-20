from Bots.Bot import Bot


class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome

    # nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    # nao esquecer o decorator
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return "Oiiii. Meu nome é {}. :)".format(self.__nome)

    def mostra_comandos(self):
        return '1 - Bom dia', '2 - Qual seu nome?', '3 - Quero um conselho', '4 - Adeus'
    
    def executa_comando(self,cmd):
        if cmd == '1':
            return 'Bom dia, Bom dia, o sol já nasceu lá na fazendinha.'
        elif cmd == '2':
            return self.apresentacao()
        elif cmd == '4':
            return self.despedida()
        else:
            return 'Ai amiguinho não tenho essa opção'
       
    def boas_vindas(self):
        return "Seja bem vindesss :)"

    def despedida(self):
        return "Adeusinho. Vou sentir sua falta :)"
