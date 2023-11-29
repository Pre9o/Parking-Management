import mysql.connector
from datetime import datetime
from mysql.connector import Error
from create_database_for_estacionamento import *
from create_tables_for_estacionamento import *
from gerencia_estacionamento import *
from gerencia_atribuicao import *
from gerencia_veiculos import *
from gerencia_veiculo_estacionado import *
from gerencia_historico import *
from menus import *

# REFACTORING: Extract Method
# TO DO: Extract Method

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"

def main():
    while True:
        print("1 - Conectar ao banco de dados")
        print("2 - Criar banco de dados")
        print("3 - Iniciar o programa")
        print("4 - Sair")
        
        option = input("Selecione a opção que você deseja gerenciar: ")

        if option == "1":
            try:
                connection = mysql.connector.connect(host='localhost',
                                            database='estacionamento',
                                            user='root',
                                            password='123456')
            
            except Error as e:
                print("Erro ao conectar ao banco de dados MySQL", e)
                
            
            if connection.is_connected():
                print('Conectado ao banco de dados MySQL')
                
            
        elif option == "2":
            create_database_for_estacionamento(host_name, user_name, user_password)
            create_tables_for_estacionamento(host_name, user_name, user_password, database_name)
            gerencia_atribuicao(host_name, user_name, user_password, database_name).criar_atribuicoes_padrao()
            gerencia_estacionamento(host_name, user_name, user_password, database_name).criar_estacionamentos_padrao()

        elif option == "3":
            menus.menu_principal(host_name, user_name, user_password, database_name)
        
        elif option == "4":
            if (connection.is_connected()):
                connection.close()
            print("Conexão ao banco de dados MySQL encerrada")
            
            break
        
        else:
            print("Opção inválida!")
            continue
            
            
if __name__ == "__main__":
    main()
