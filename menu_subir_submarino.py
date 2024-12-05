import os

class MenuSubirSumarino:

    def __init__(self, bluetooth_connection):
        self.__bluetooth_connection = bluetooth_connection

    def separador_de_linha(self):
        """
        Printa um separador de linha
        :return:
        """
        print("-" * 90)

    def apresentacao_menu(self):

        self.separador_de_linha()
        print("""
        
░██████╗██╗░░░██╗██████╗░██╗███╗░░██╗██████╗░░█████╗░░░░░░░░░░
██╔════╝██║░░░██║██╔══██╗██║████╗░██║██╔══██╗██╔══██╗░░░░░░░░░
╚█████╗░██║░░░██║██████╦╝██║██╔██╗██║██║░░██║██║░░██║░░░░░░░░░
░╚═══██╗██║░░░██║██╔══██╗██║██║╚████║██║░░██║██║░░██║░░░░░░░░░
██████╔╝╚██████╔╝██████╦╝██║██║░╚███║██████╔╝╚█████╔╝██╗██╗██╗
╚═════╝░░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝╚═╝╚═╝
        """)
        self.separador_de_linha()

    def __mostrar_opcoes(self):
        """
        Apresenta do menu
        :return:
        """
        print(f"1 {'-' * 25} Parar submarino")

    def __perguntar_pela_parada(self):
        """
        Para o submarino
        :return:
        """
        while True:

            try:
                resposta = int(input("Digite a opcao: "))

                match resposta:
                    case 1:
                        self.__bluetooth_connection.send("3")
                        print("parando submarino")
                        break

                    case _:
                        print("opcao invalida")
            except ValueError:
                print("Digite um numero")

    def main(self):
        os.system("cls")
        self.__bluetooth_connection.send("2")
        self.apresentacao_menu()
        self.__mostrar_opcoes()
        self.separador_de_linha()
        self.__perguntar_pela_parada()