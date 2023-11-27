import mysql.connector
import random
from mysql.connector import Error
from criar_sql import *
from gerencia_estacionamento import *

host_name = "localhost"
user_name = "root"
user_password = "123456"
lista = []

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
    id_estacionamento = input("Digite o novo id do estacionamento: ")
    gerencia_veiculos(host_name, user_name, user_password, database_name).update_veiculo(placa, nova_placa,modelo, dono_do_veiculo, id_estacionamento)
    
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
