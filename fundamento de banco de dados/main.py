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
    
    gerencia_veiculos(host_name, user_name, user_password, database_name).criar_veiculo(placa, modelo, usuario)
    
    print("Veículo adicionado com sucesso!")

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
                print("4 - Listar usuários")
                print("5 - Listar veículos")
                print("6 - Listar atribuições")
                print("7 - Atualizar usuário")
                print("8 - Atualizar veículo")
                print("9 - Atualizar atribuição")
                print("10 - Remover usuário")
                print("11 - Remover veículo")
                print("12 - Remover atribuição")
                print("13 - Criar DataBase")
                print("14 - Criar tabelas")
                print("15 - Sair")

                opcao = int(input("Digite a opção desejada: "))
                
                if opcao == 1:
                    adicionar_atribuicao(host_name, user_name, user_password, database_name)
                
                elif opcao == 2:
                    adicionar_usuario(host_name, user_name, user_password, database_name)
                
                elif opcao == 3:
                    adicionar_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 4:
                    lista = gerencia_usuarios(host_name, user_name, user_password, database_name).read_usuarios()
                    for i in lista:
                        print(i)

                elif opcao == 5:
                    lista = gerencia_veiculos(host_name, user_name, user_password, database_name).read_veiculos()
                    for i in lista:
                        print(i)

                elif opcao == 6:
                    lista = gerencia_atribuicao(host_name, user_name, user_password, database_name).read_atribuicao()
                    for i in lista:
                        print(i)
                
                elif opcao == 7:
                    atualizar_usuario(host_name, user_name, user_password, database_name)

                elif opcao == 8:
                    atualizar_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 9:
                    atualizar_atribuicao(host_name, user_name, user_password, database_name)

                elif opcao == 10:
                    remover_usuario(host_name, user_name, user_password, database_name)

                elif opcao == 11:
                    remover_veiculo(host_name, user_name, user_password, database_name)

                elif opcao == 12:
                    remover_atribuicao(host_name, user_name, user_password, database_name)
        
                elif opcao == 13:
                    create_database_for_estacionamento(host_name, user_name, user_password)

                elif opcao == 14:
                    create_tables_for_estacionamento(host_name, user_name, user_password, database_name)

                elif opcao == 15:
                    break
            
            
    except Error as e:
        print("Erro ao conectar ao banco de dados MySQL", e)
        
    finally:
        if (connection.is_connected()):
            connection.close()
            print("Conexão ao banco de dados MySQL encerrada")
            




main()
