from gerencia_usuarios import gerencia_usuarios
from gerencia_veiculos import gerencia_veiculos
from gerencia_atribuicao import gerencia_atribuicao
from gerencia_estacionamento import gerencia_estacionamento
from adicoes import adicoes
from atualizacoes import atualizacoes
from remocoes import *
from vigilante import vigilante

class menus():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name

    def menu_vigilante(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Entrada de veículo")
            print("2 - Saída de veículo")
            print("3 - Voltar")

            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                vigilante.entrada_veiculo(host_name, user_name, user_password, database_name)

            elif opcao == 2:
                vigilante.saida_veiculo(host_name, user_name, user_password, database_name)

            elif opcao == 3:
                break

            else:
                print("Opção inválida!")
                continue

    def menu_usuarios(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Adicionar usuário")
            print("2 - Listar usuários")
            print("3 - Atualizar usuário")
            print("4 - Remover usuário")
            print("5 - Voltar")

            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                adicoes.adicionar_usuario(host_name, user_name, user_password, database_name, False)
            
            elif opcao == 2:
                lista = gerencia_usuarios(host_name, user_name, user_password, database_name).read_usuarios()
                for i in lista:
                    print(i)

            elif opcao == 3:
                atualizacoes.atualizar_usuario(host_name, user_name, user_password, database_name)

            elif opcao == 4:
                remocoes.remover_usuario(host_name, user_name, user_password, database_name)
            
            elif opcao == 5:
                break

            else:
                print("Opção inválida!")
                continue

    def menu_veiculos(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Adicionar veículo")
            print("2 - Listar veículos")
            print("3 - Atualizar veículo")
            print("4 - Remover veículo")
            print("5 - Voltar")

            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                adicoes.adicionar_veiculo(host_name, user_name, user_password, database_name)
            
            elif opcao == 2:
                lista = gerencia_veiculos(host_name, user_name, user_password, database_name).read_veiculos()
                for i in lista:
                    print(i)

            elif opcao == 3:
                atualizacoes.atualizar_veiculo(host_name, user_name, user_password, database_name)

            elif opcao == 4:
                remocoes.remover_veiculo(host_name, user_name, user_password, database_name)
            
            elif opcao == 5:
                break

            else:
                print("Opção inválida!")
                continue


    def menu_atribuicao(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Adicionar atribuição")
            print("2 - Listar atribuições")
            print("3 - Atualizar atribuição")
            print("4 - Remover atribuição")
            print("5 - Voltar")

            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                adicoes.adicionar_atribuicao(host_name, user_name, user_password, database_name)
            
            elif opcao == 2:
                lista = gerencia_atribuicao(host_name, user_name, user_password, database_name).read_atribuicao()
                for i in lista:
                    print(i)

            elif opcao == 3:
                atualizacoes.atualizar_atribuicao(host_name, user_name, user_password, database_name)

            elif opcao == 4:
                remocoes.remover_atribuicao(host_name, user_name, user_password, database_name)
            
            elif opcao == 5:
                break

            else:
                print("Opção inválida!")
                continue

    def menu_estacionamento(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Adicionar estacionamento")
            print("2 - Listar estacionamentos")
            print("3 - Atualizar estacionamento")
            print("4 - Remover estacionamento")
            print("5 - Voltar")

            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                adicoes.adicionar_estacionamento(host_name, user_name, user_password, database_name)
            
            elif opcao == 2:
                lista = gerencia_estacionamento(host_name, user_name, user_password, database_name).read_estacionamento()
                for i in lista:
                    print(i)

            elif opcao == 3:
                atualizacoes.atualizar_estacionamento(host_name, user_name, user_password, database_name)

            elif opcao == 4:
                remocoes.remover_estacionamento(host_name, user_name, user_password, database_name)
            
            elif opcao == 5:
                break

            else:
                print("Opção inválida!")
                continue

    def menu_gerenciamento(host_name, user_name, user_password, database_name):
        while True:
                    print("1 - Gerenciar usuários")
                    print("2 - Gerenciar veículos")
                    print("3 - Gerenciar atribuições")
                    print("4 - Gerenciar estacionamentos")
                    print("5 - Sair")

                    option = input("Selecione a opção que você deseja gerenciar: ")

                    if option == "1":
                        menus.menu_usuarios(host_name, user_name, user_password, database_name)
                        
                    elif option == "2":
                        menus.menu_veiculos(host_name, user_name, user_password, database_name)

                    elif option == "3":
                        menus.menu_atribuicao(host_name, user_name, user_password, database_name)

                    elif option == "4":
                        menus.menu_estacionamento(host_name, user_name, user_password, database_name)

                    elif option == "5":
                        break

                    else:
                        print("Opção inválida!")
                        continue

    def menu_principal(host_name, user_name, user_password, database_name):
        while True:
            print("1 - Menu de gerenciamento")
            print("2 - Menu do vigilante")
            print("3 - Sair")

            option = input("Selecione a opção que você deseja gerenciar: ")

            if option == "1":
                menus.menu_gerenciamento(host_name, user_name, user_password, database_name)

            elif option == "2":
                menus.menu_vigilante(host_name, user_name, user_password, database_name)

            elif option == "3":
                break
            
            else:
                print("Opção inválida!")
                continue