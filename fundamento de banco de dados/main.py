import mysql.connector
import random
from mysql.connector import Error
from criar_sql import *
from gerencia_estacionamento import *

host_name = "localhost"
user_name = "root"
user_password = "123456"
<<<<<<< Updated upstream
lista = []
=======
database_name = "estacionamento"

def entrada_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo: ").upper()
    placa = verificacao(placa,"placa")
    id_estacionamento = input("Digite o id do estacionamento: ")
    codigo_de_barra = gerencia_veiculos(host_name, user_name, user_password, database_name).read_codigo_de_barra(placa)

    while True:
        option = input("Quer utilizar a data e hora atual? (S/N): ").upper()
        if option == "S":
            data_hora_entrada = datetime.now()
            break
        elif option == "N":
            data = input("Digite a data: ")
            hora = input("Digite a hora: ")
            data_hora_entrada = data + " " + hora
            break
        else:
            print("Opção inválida!")
            continue

        
    gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).criar_veiculo_estacionado(placa, codigo_de_barra, id_estacionamento, data_hora_entrada)
    gerencia_historico(host_name, user_name, user_password, database_name).criar_historico(placa, id_estacionamento, data_hora_entrada, data_saida=None)
    print("Entrada realizada com sucesso!")



def saida_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do carro: ")
    placa = verificacao(placa,"placa")
    data_hora_entrada = gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).read_data_entrada(placa)
    id_estacionamento = gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).get_id_estacionamento(placa)


    while True:
        option = input("Quer utilizar a data e hora atual? (S/N): ").upper()
        if option == "S":
            data_hora_saida = datetime.now()
            break
        elif option == "N":
            data = input("Digite a data: ")
            hora = input("Digite a hora: ")
            data_hora_saida = data + " " + hora
            break
        else:
            print("Opção inválida!")
            continue
        
    gerencia_historico(host_name, user_name, user_password, database_name).update_historico(placa, id_estacionamento, data_hora_entrada, data_hora_saida)
    gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).deletar_veiculo_estacionado(placa)
    
    print("Saída realizada com sucesso!") 
    

def menu_gerenciamento(host_name, user_name, user_password, database_name):
    while True:
                print("1 - Gerenciar usuários")
                print("2 - Gerenciar veículos")
                print("3 - Gerenciar atribuições")
                print("4 - Gerenciar estacionamentos")
                print("5 - Sair")

                option = input("Selecione a opção que você deseja gerenciar: ")

                if option == "1":
                    menu_usuarios(host_name, user_name, user_password, database_name)
                    
                elif option == "2":
                    menu_veiculos(host_name, user_name, user_password, database_name)

                elif option == "3":
                    menu_atribuicao(host_name, user_name, user_password, database_name)

                elif option == "4":
                    menu_estacionamento(host_name, user_name, user_password, database_name)

                elif option == "5":
                    break

                else:
                    print("Opção inválida!")
                    continue


def menu_vigilante(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Voltar")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            entrada_veiculo(host_name, user_name, user_password, database_name)

        elif opcao == 2:
            saida_veiculo(host_name, user_name, user_password, database_name)

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
            adicionar_usuario(host_name, user_name, user_password, database_name, False)
        
        elif opcao == 2:
            lista = gerencia_usuarios(host_name, user_name, user_password, database_name).read_usuarios()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_usuario(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_usuario(host_name, user_name, user_password, database_name)
        
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
            adicionar_veiculo(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_veiculos(host_name, user_name, user_password, database_name).read_veiculos()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_veiculo(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_veiculo(host_name, user_name, user_password, database_name)
        
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
            adicionar_atribuicao(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_atribuicao(host_name, user_name, user_password, database_name).read_atribuicao()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_atribuicao(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_atribuicao(host_name, user_name, user_password, database_name)
        
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
            adicionar_estacionamento(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_estacionamento(host_name, user_name, user_password, database_name).read_estacionamento()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_estacionamento(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_estacionamento(host_name, user_name, user_password, database_name)
        
        elif opcao == 5:
            break

        else:
            print("Opção inválida!")
            continue

>>>>>>> Stashed changes

def adicionar_atribuicao(host_name, user_name, user_password, database_name):
    nome_atribuicao = input("Digite o nome da atribuição: ").capitalize()
    id_atribuicao = input("Digite o id da atribuição: ")
    
    gerencia_atribuicao(host_name, user_name, user_password, database_name).criar_atribuicao(id_atribuicao, nome_atribuicao)
    
    print("Atribuição adicionada com sucesso!")


def adicionar_usuario(host_name, user_name, user_password, database_name):
    nome = input("Digite o nome do usuário: ").capitalize()
    atribuicao = input("Digite o nome da atribuição do usuário: ")
    codigo_de_barra = gerencia_usuarios(host_name, user_name, user_password, database_name).get_codigos_de_barra()
    atribuicao = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
    gerencia_usuarios(host_name, user_name, user_password, database_name).criar_usuario(nome, atribuicao, codigo_de_barra)
    
    print("Usuário adicionado com sucesso!")

                            
def adicionar_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo: ").upper()
    modelo = input("Digite o modelo do veículo: ").capitalize()
    usuario = input("Digite o codigo do dono: ")
    id_estacionamento = input("Digite o id do estacionamento: ")
    
    gerencia_veiculos(host_name, user_name, user_password, database_name).criar_veiculo(placa, modelo, usuario, id_estacionamento)
    
    print("Veículo adicionado com sucesso!")

<<<<<<< Updated upstream
=======

def verificacao(verifica, tipo):
    if tipo == "usuario":
        verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
        
        while verificacao_codigo == None:
            print("Usuário não encontrado!")
            codigo_de_barra = input("Digite o código de barra do usuário: ")
            verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
        
        return codigo_de_barra
    
    elif tipo == "veiculo":

        verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(usuario)
        while verifica == None:
            print("Usuário não encontrado!")
            print("1- Digitar novamente o código do dono: ")
            print("2- Criar um novo usuário")
            option = input("Digite a opção desejada: ")
            if option == "1":
                usuario = input("Digite o codigo do dono: ")
                verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(usuario)
            elif option == "2":
                usuario = adicionar_usuario(host_name, user_name, user_password, database_name, True)
                verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(usuario)
        
        return verifica
    
    elif tipo == "atribuicao":
        
        verifica = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
        while verifica == None:
            print("Atribuição não encontrada!")
            atribuicao = input("Digite o nome da atribuição: ").capitalize()
            verifica = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
        
        return verifica
    
    elif tipo == "placa":
        
        verifica = gerencia_veiculos(host_name, user_name, user_password, database_name).get_placa(verifica)
        while verifica == None:
            print("Carro não encontrado!")
            verifica = input("Digite novamente a placa do veículo: ").upper()
            verifica = gerencia_veiculos(host_name, user_name, user_password, database_name).get_placa(verifica)
        
        return verifica
    
    elif tipo == "estacionamento":
            
            verifica = gerencia_estacionamento(host_name, user_name, user_password, database_name).get_estacionamento(verifica)
            while verifica == None:
                print("Estacionamento não encontrado!")
                verifica = input("Digite o id do estacionamento: ")
                verifica = gerencia_estacionamento(host_name, user_name, user_password, database_name).get_estacionamento(verifica)
            
            return verifica
    


>>>>>>> Stashed changes
def adicionar_estacionamento(host_name, user_name, user_password, database_name):
    id_estacionamento = input("Digite o id do estacionamento: ")
    gerencia_estacionamento(host_name, user_name, user_password, database_name).criar_estacionamento(id_estacionamento)
    
    print("Estacionamento adicionado com sucesso!")


def atualizar_usuario(host_name, user_name, user_password, database_name):
    codigo_de_barra = input("Digite o código de barra do usuário que quer atualizar: ")
    nome_usuario = input("Digite o novo nome do usuário: ").capitalize()
    atribuicao = input("Digite a nova atribuição do usuário: ").capitalize()
    gerencia_usuarios(host_name, user_name, user_password, database_name).update_usuario(nome_usuario, atribuicao, codigo_de_barra)
    
    print("Usuário atualizado com sucesso!")

def atualizar_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo que quer atualizar: ").upper()
    modelo = input("Digite o novo modelo do veículo: ").capitalize()
    dono_do_veiculo = input("Digite o novo dono do veículo: ").capitalize()
    nova_placa = input("Digite a nova placa do veículo: ").upper()
    gerencia_veiculos(host_name, user_name, user_password, database_name).update_veiculo(placa, nova_placa,modelo, dono_do_veiculo)
    
    print("Veículo atualizado com sucesso!")

def atualizar_atribuicao(host_name, user_name, user_password, database_name):
    id_atribuicao = input("Digite o id da atribuição que quer atualizar: ")
    nome_atribuicao = input("Digite o novo nome da atribuição: ").capitalize()
    gerencia_atribuicao(host_name, user_name, user_password, database_name).update_atribuicao(nome_atribuicao, id_atribuicao)
    
    print("Atribuição atualizada com sucesso!")

def atualizar_estacionamento(host_name, user_name, user_password, database_name):
    id_estacionamento = input("Digite o id do estacionamento que quer atualizar: ")
    novo_id_estacionamento = input("Digite o novo id do estacionamento: ")

    gerencia_estacionamento(host_name, user_name, user_password, database_name).update_estacionamento(id_estacionamento, novo_id_estacionamento)
    
    print("Estacionamento atualizado com sucesso!")


def remover_usuario(host_name, user_name, user_password, database_name):
    codigo_de_barra = input("Digite o código de barra do usuário que quer remover: ")
    gerencia_usuarios(host_name, user_name, user_password, database_name).deletar_usuario(codigo_de_barra)
    
    print("Usuário removido com sucesso!")


def remover_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo que quer remover: ").upper()
    gerencia_veiculos(host_name, user_name, user_password, database_name).deletar_veiculo(placa)
    
    print("Veículo removido com sucesso!")

def remover_atribuicao(host_name, user_name, user_password, database_name):
    id_atribuicao = input("Digite o id da atribuição que quer remover: ")
    gerencia_atribuicao(host_name, user_name, user_password, database_name).deletar_atribuicao(id_atribuicao)
    
    print("Atribuição removida com sucesso!")

def remover_estacionamento(host_name, user_name, user_password, database_name):
    id_estacionamento = input("Digite o id do estacionamento que quer remover: ")
    gerencia_estacionamento(host_name, user_name, user_password, database_name).deletar_estacionamento(id_estacionamento)
    
    print("Estacionamento removido com sucesso!")









def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='estacionamento',
                                             user='root',
                                             password='123456')

        if connection.is_connected():
            print('Conectado ao banco de dados MySQL')


            while True:
                print("1 - Adicionar atribuição")
                print("2 - Adicionar usuário")
                print("3 - Adicionar veículo")
                print("4 - Adicionar estacionamento")
                print("5 - Listar usuários")
                print("6 - Listar veículos")
                print("7 - Listar atribuições")
                print("8 - Atualizar usuário")
                print("9 - Atualizar veículo")
                print("10 - Atualizar atribuição")
                print("11 - Remover usuário")
                print("12 - Remover veículo")
                print("13 - Remover atribuição")
                print("14 - Criar DataBase")
                print("15 - Criar Tabelas")
                print("16 - Sair")

                opcao = int(input("Digite a opção desejada: "))
                
                if opcao == 1:
                    adicionar_atribuicao(host_name, user_name, user_password, database_name)
                
                elif opcao == 2:
                    adicionar_usuario(host_name, user_name, user_password, database_name)
                
                elif opcao == 3:
                    adicionar_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 4:
                    adicionar_estacionamento(host_name, user_name, user_password, database_name)

                elif opcao == 5:
                    lista = gerencia_usuarios(host_name, user_name, user_password, database_name).read_usuarios()
                    for i in lista:
                        print(i)

                elif opcao == 6:
                    lista = gerencia_veiculos(host_name, user_name, user_password, database_name).read_veiculos()
                    for i in lista:
                        print(i)

                elif opcao == 7:
                    lista = gerencia_atribuicao(host_name, user_name, user_password, database_name).read_atribuicao()
                    for i in lista:
                        print(i)
                
                elif opcao == 8:
                    atualizar_usuario(host_name, user_name, user_password, database_name)

                elif opcao == 9:
                    atualizar_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 10:
                    atualizar_atribuicao(host_name, user_name, user_password, database_name)

                elif opcao == 11:
                    remover_usuario(host_name, user_name, user_password, database_name)

                elif opcao == 12:
                    remover_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 13:
                    remover_atribuicao(host_name, user_name, user_password, database_name)
        
                elif opcao == 14:
                    create_database_for_estacionamento(host_name, user_name, user_password)

                elif opcao == 15:
                    create_tables_for_estacionamento(host_name, user_name, user_password, database_name)

                elif opcao == 16:
                    break
            
            
    except Error as e:
        print("Erro ao conectar ao banco de dados MySQL", e)
        
    finally:
        if (connection.is_connected()):
            connection.close()
            print("Conexão ao banco de dados MySQL encerrada")
            




main()
