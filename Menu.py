from menu_subir_submarino import MenuSubirSumarino
from menu_descer_submarino import MenuDescerSumarino
import os

class Menu:
    def __init__(self, bluetooth_connection):
        self.__bluetooth_connection = bluetooth_connection

    def separador_de_linha(self):
        """
        Printa um separador de linha
        :return:
        """
        print("-" * 90)
    def __apresentacao_sistema(self):
        """
        Apresenta do sistema
        :return:
        """
        self.separador_de_linha()
        print("""
░██████╗██╗░░░██╗██████╗░███╗░░░███╗░█████╗░██████╗░██╗███╗░░██╗░█████╗░
██╔════╝██║░░░██║██╔══██╗████╗░████║██╔══██╗██╔══██╗██║████╗░██║██╔══██╗
╚█████╗░██║░░░██║██████╦╝██╔████╔██║███████║██████╔╝██║██╔██╗██║██║░░██║
░╚═══██╗██║░░░██║██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗██║██║╚████║██║░░██║
██████╔╝╚██████╔╝██████╦╝██║░╚═╝░██║██║░░██║██║░░██║██║██║░╚███║╚█████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░
""")
        self.separador_de_linha()

    def __apresentar_menu(self):
        """
        Apresenta do menu
        :return:
        """
        print(f"1 {'-' * 25} Subir submarino")
        print(f"2 {'-' * 25} Descer submarino")

    def __perguntar_sobre_opcao_menu_principal(self):
        """
        Pergunta sobre opcao do menu
        :return:
        """
        while True:
            try:
                resposta = int(input("Digite a opção selecionada: "))

                match resposta:
                    case 1:
                        menu_submarino_subir = MenuSubirSumarino(self.__bluetooth_connection)
                        menu_submarino_subir.main()
                        self.main()
                        break
                    case 2:
                        menu_descer_submarino = MenuDescerSumarino(self.__bluetooth_connection)
                        menu_descer_submarino.main()
                        self.main()
                        break
                    case _:
                        print("Opcao invalida")


            except ValueError:
                print("Por favor digite um numero válido")

    def main(self):
        """
        It runs all the needed stuf
        :return:
        """
        os.system("cls")

        self.__apresentacao_sistema()

        self.__apresentar_menu()

        self.__perguntar_sobre_opcao_menu_principal()