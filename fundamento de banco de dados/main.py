import mysql.connector
import random
from mysql.connector import Error
from criar_sql import *
from gerencia_estacionamento import *

host_name = "localhost"
user_name = "root"
user_password = "123456"

def adicionar_atribuicao(host_name, user_name, user_password, database_name):
    nome_atribuicao = input("Digite o nome da atribuição: ")
    id_atribuicao = input("Digite o id da atribuição: ")
    
    gerencia_atribuicao(host_name, user_name, user_password, database_name).criar_atribuicao(nome_atribuicao, id_atribuicao)
    
    print("Atribuição adicionada com sucesso!")


def adicionar_usuario(host_name, user_name, user_password, database_name):
    nome = input("Digite o nome do usuário: ")
    atribuicao = input("Digite a atribuição do usuário: ")
    codigo_de_barra = gerencia_usuarios(host_name, user_name, user_password, database_name).get_codigos_de_barra()
    atribuicao = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
    gerencia_usuarios(host_name, user_name, user_password, database_name).criar_usuario(nome, atribuicao, codigo_de_barra)
    
    print("Usuário adicionado com sucesso!")
    
                            
def adicionar_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    usuario = input("Digite o nome do usuário: ")
    
    gerencia_veiculos(host_name, user_name, user_password, database_name).criar_veiculo(placa, modelo, usuario)
    
    print("Veículo adicionado com sucesso!")

def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='estacionamento',
                                             user='root',
                                             password='123456')

        if connection.is_connected():
            print('Conectado ao banco de dados MySQL')

            create_database_for_estacionamento(host_name, user_name, user_password)
            create_tables_for_estacionamento(host_name, user_name, user_password, database_name)
            
            adicionar_usuario(host_name, user_name, user_password, database_name)
            
    except Error as e:
        print("Erro ao conectar ao banco de dados MySQL", e)
        
    finally:
        if (connection.is_connected()):
            connection.close()
            print("Conexão ao banco de dados MySQL encerrada")
            

main()
