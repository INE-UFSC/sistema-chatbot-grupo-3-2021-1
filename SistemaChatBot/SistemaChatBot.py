from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nome_empresa: str, lista_bots: list):
        self.__empresa = nome_empresa
        self.__lista_bots = [bot for bot in lista_bots if type(bot) == Bot]
        self.__bot = None
    
    def boas_vindas(self):
        print("Seja bem-vindo(a) ao sistema Chat Bot da empresa", self.__empresa, end='\n\n')

    def mostra_menu(self):
        print("Os bots disponíveis são:")
        for bot in self.__lista_bots:
            print()
    
    def escolhe_bot(self):
        pass
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
