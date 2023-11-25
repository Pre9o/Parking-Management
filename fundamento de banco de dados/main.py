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
    
    connection = connect_sql.create_server_connection(connect_sql, host_name, user_name, user_password, database_name)
    connection.autocommit = True
    
    query = f"INSERT INTO {database_name}.atribuicao (id_atribuicao, nome_atribuicao) VALUES ('{id_atribuicao}', '{nome_atribuicao}')"
        
    connect_sql.execute_query(connection, query)
    
    print("Atribuição adicionada com sucesso!")
    
    connection.close()
    
    return nome_atribuicao

def procurar_atribuicao(nome_atribuicao, host_name, user_name, user_password, database_name):
    connection = connect_sql.create_server_connection(connect_sql, host_name, user_name, user_password, database_name)
    connection.autocommit = True
    
    query = f"SELECT id_atribuicao FROM {database_name}.atribuicao WHERE nome_atribuicao = '{nome_atribuicao}'"
    
    id_atribuicao = connect_sql.execute_read_query(connection, query)
    
    connection.close()
    
    return id_atribuicao[0][0]
    
    
def gerador_codigo_de_barra(database_name):
    codigo_gerado = random.randint(1000000000, 9999999999)
    
    codigos_existentes = []
    
    connection = connect_sql.create_server_connection(connect_sql, host_name, user_name, user_password, database_name)
    connection.autocommit = True
    
    codigos = connect_sql.execute_read_query(connection, f"SELECT codigo_de_barra FROM {database_name}.usuario")
    
    for codigo in codigos:
        codigos_existentes.append(codigo[0])
        
    while codigo_gerado in codigos_existentes:
        codigo_gerado = random.randint(1000000000, 9999999999)
        
    connection.close()
    
    return codigo_gerado


def adicionar_usuario(host_name, user_name, user_password, database_name):
    nome = input("Digite o nome do usuário: ")
    atribuicao = input("Digite a atribuição do usuário: ").lower()
    codigo_de_barra = gerador_codigo_de_barra(database_name)

    atribuicao = procurar_atribuicao(atribuicao, host_name, user_name, user_password, database_name)
    
    connection = connect_sql(host_name, user_name, user_password, database_name)
    
    query = f"INSERT INTO {database_name}.usuario (nome_usuario, atribuicao_id_atribuicao, codigo_de_barra) VALUES ('{nome}', '{atribuicao}', '{codigo_de_barra}')"
    
    connection.insert_into_table(query)
    
    
    print("Usuário adicionado com sucesso!")  
    
                            
def adicionar_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    usuario = input("Digite o nome do usuário: ")
    
    connection = connect_sql(host_name, user_name, user_password, database_name)
    
    query = f"INSERT INTO {database_name}.veiculo (placa, modelo, cor, ano, usuario_codigo_de_barra) VALUES ('{placa}', '{modelo}', '{cor}', '{ano}', '{usuario}')"
    
    connection.insert_into_table(query)
    
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
