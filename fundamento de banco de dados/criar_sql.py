import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"


class create_database_for_estacionamento():
    def __init__(self, host_name, user_name, user_password):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.define_database(host_name, user_name, user_password)
    
    def create_server_connection(self, host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
            
    def create_database(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def define_database(self, host_name, user_name, user_password):
        connection = self.create_server_connection(host_name, user_name, user_password)
        query = "CREATE DATABASE estacionamento"
        self.create_database(connection, query)
        connection.close()
        
        
class create_tables_for_estacionamento():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.define_table_atribuicao(host_name, user_name, user_password, database_name)
        
    def create_server_connection(self, host_name, user_name, user_password, database_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
            
    def create_table(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Table created successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def define_table_atribuicao(self, host_name, user_name, user_password, database_name):
        connection = self.create_server_connection(host_name, user_name, user_password, database_name)
        query = """CREATE TABLE atribuicao (
                    id_atribuicao INT NOT NULL,
                    nome_atribuicao VARCHAR(45) NOT NULL,
                    PRIMARY KEY (id_atribuicao)
                    )"""
                    
        self.create_table(connection, query)
        
        query = """CREATE TABLE usuario (
                    nome_usuario VARCHAR(45) NOT NULL,
                    atribuicao_id_atribuicao INT NOT NULL,
                    codigo_de_barra VARCHAR(45) NOT NULL,
                    PRIMARY KEY (codigo_de_barra),
                    FOREIGN KEY (atribuicao_id_atribuicao) REFERENCES atribuicao (id_atribuicao)
                    )"""
        
        self.create_table(connection, query)
        
        query = """CREATE TABLE veiculo (
                    placa_veiculo VARCHAR(45) NOT NULL,
                    modelo_veiculo VARCHAR(45) NOT NULL,
                    dono_do_veiculo VARCHAR(45) NOT NULL,
                    PRIMARY KEY (placa_veiculo),
                    FOREIGN KEY (dono_do_veiculo) REFERENCES usuario (codigo_de_barra)
                    )"""
                    
        self.create_table(connection, query)
        
        query = """CREATE TABLE estacionamentos (
                    id_estacionamento INT NOT NULL,
                    placa_veiculo_estacionado VARCHAR(45) NOT NULL,
                    PRIMARY KEY (id_estacionamento),
                    FOREIGN KEY (placa_veiculo_estacionado) REFERENCES veiculo (placa_veiculo)
                    )"""
                    
        self.create_table(connection, query)
        
        query = """CREATE TABLE historico (
                    id_historico INT NOT NULL,
                    placa_veiculo VARCHAR(45) NOT NULL,
                    estacionamento_id_estacionamento INT NOT NULL,
                    data_entrada DATETIME NOT NULL,
                    data_saida DATETIME NOT NULL,
                    PRIMARY KEY (id_historico),
                    FOREIGN KEY (placa_veiculo) REFERENCES veiculo (placa_veiculo),
                    FOREIGN KEY (estacionamento_id_estacionamento) REFERENCES estacionamentos (id_estacionamento)
                    )"""
                    
        self.create_table(connection, query)
        
        connection.close()
        
