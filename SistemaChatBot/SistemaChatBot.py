from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nome_empresa: str, lista_bots: list):
        self.__empresa = nome_empresa
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print("Seja bem-vindo(a) ao sistema Chat Bot da empresa", self.__empresa, end='\n\n')

    def mostra_menu(self):
        print("Os bots disponíveis são:")
        for bot in self.__lista_bots:
            print(self.__lista_bots.index(bot), '-', bot.nome, '->', 'apresentação:', bot.apresentacao())
        print()

    def escolhe_bot(self):
        resposta = str(input("Escolha um bot: "))
        self.__bot = self.__lista_bots[int(resposta)]
        print(self.__bot.boas_vindas())

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        self.le_envia_comando()

    def le_envia_comando(self):
        cmd = str(input("   -> Digite o comando: "))
        if cmd == '-1' or cmd == '4':
            print(self.__bot.despedida())
        else:
            print(self.__bot.executa_comando(cmd))
            self.mostra_comandos_bot()

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.mostra_comandos_bot()

        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
