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
    def nome(nome, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return "Oiiii. Meu nome é {}. :)".format(self.__nome)

    def mostra_comandos(self):
        return '1 - Bom dia \n2 - Qual seu nome? \n3 - Quero um conselho \n4 - Adeus'
    
    def executa_comando(self,cmd):
        if cmd == '1':
            return 'Bom dia, Bom dia, o sol já nasceu lá na fazendinha.'
        elif cmd == '2':
            return self.apresentcao()
        elif cmd == '3':
            return 'Não ligue para os outros, SEJA FELIZ'
        else:
           return self.despedida()         
       
    def boas_vindas(self):
        return "Seja bem vindesss :)"

    def despedida(self):
        return "Adeusinho. Vou sentir sua falta :)"
