from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return f'Oi eu sou o {self.__nome} um gotico triste'
 
    def mostra_comandos(self):
        return '1 - Bom dia', '2 - Qual seu nome?', '3 - Quero um conselho', '4 - Adeus'
    
    def executa_comando(self,cmd):
        if cmd == '1':
            return 'Estou sad hoje, nao é um bom dia'
        elif cmd == '2':
            return 'estou na bad pra dizer meu nome e eu ja disse'
        elif cmd == '3':
            return 'Fique com os amigos, sempre ou vai ficar na bad igual a mim' 
        else:
            return BotTriste.despedida()

    def boas_vindas(self):
        return 'Bem vindo mas sei que vc ja vai'

    def despedida(self):
        return 'Ate nunca mais!!'

    
    
    