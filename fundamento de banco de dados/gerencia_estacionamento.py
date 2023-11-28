import mysql.connector
import random
from mysql.connector import Error
from criar_sql import *

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"

class connect_sql():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = self.create_server_connection(host_name, user_name, user_password, database_name)
        self.cursor = self.connection.cursor()
        
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
    
    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    
    def execute_read_query(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
            
    def close_connection(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
            
    def insert_into_table(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Insert into table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def select_from_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
            
    def delete_from_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Delete from table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def update_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Update table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
class gerencia_atribuicao():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_atribuicao(self, id_atribuicao, nome_atribuicao):
        query = f"""INSERT INTO atribuicao (id_atribuicao, nome_atribuicao)
                    VALUES ('{id_atribuicao}', '{nome_atribuicao}')"""
        self.connection.insert_into_table(query)
        
    def read_atribuicao(self):
        query = f"""SELECT * FROM atribuicao"""
        result = self.connection.select_from_table(query)
        return result
    
    def get_atribuicao(self, nome_atribuicao):
        query = f"""SELECT id_atribuicao FROM atribuicao 
                WHERE nome_atribuicao = '{nome_atribuicao}'"""
        result = self.connection.execute_read_query(query)
        if result:
            return result[0][0]  # Acessa o primeiro elemento da primeira tupla
        else:
            return None  # ou outra indicação de valor não encontrado, se desejado
    
    def update_atribuicao(self, nome_atribuicao, id_atribuicao):
        query = f"""UPDATE atribuicao SET nome_atribuicao = '{nome_atribuicao}'
                    WHERE id_atribuicao = '{id_atribuicao}'"""
        self.connection.update_table(query)
        
    def deletar_atribuicao(self, id_atribuicao):
        query = f"""DELETE FROM atribuicao WHERE id_atribuicao = '{id_atribuicao}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()
            

class gerencia_usuarios():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_usuario(self, nome_usuario, atribuicao_usuario, codigo_de_barra):
        query = f"""INSERT INTO usuario (nome_usuario, atribuicao_id_atribuicao, codigo_de_barra)
                    VALUES ('{nome_usuario}', '{atribuicao_usuario}', '{codigo_de_barra}')"""
        self.connection.insert_into_table(query)
        
    def read_usuarios(self):
        query = f"""SELECT * FROM usuario"""
        result = self.connection.select_from_table(query)
        return result
    
    def get_codigos_de_barra(self):
        query = f"""SELECT codigo_de_barra FROM usuario"""
        result = self.connection.execute_read_query(query)
        
        codigo_gerado = random.randint(100000000000, 999999999999)
        
        while codigo_gerado in result:
            codigo_gerado = random.randint(100000000000, 999999999999)
        
        return codigo_gerado
    
    def update_usuario(self, nome_usuario, atribuicao_usuario, codigo_de_barra):
        query = f"""UPDATE usuario SET nome_usuario = '{nome_usuario}', atribuicao_id_atribuicao = '{atribuicao_usuario}'
                    WHERE codigo_de_barra = '{codigo_de_barra}'"""
        self.connection.update_table(query)
        
    def deletar_usuario(self, codigo_de_barra):
        query = f"""DELETE FROM usuario WHERE codigo_de_barra = '{codigo_de_barra}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()
        
        
class gerencia_veiculos():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_veiculo(self, placa_veiculo, modelo_veiculo, codigo_de_barra_dono, id_estacionamento):
        query = f"""INSERT INTO veiculo (placa_veiculo, modelo_veiculo, dono_do_veiculo, estacionamento_id_estacionamento)
                    VALUES ('{placa_veiculo}', '{modelo_veiculo}', '{codigo_de_barra_dono}', '{id_estacionamento}')"""
        self.connection.insert_into_table(query)
        query = f"""INSERT INTO estac_veic (veiculo_placa_veiculo, estacionamentos_id_estacionamento)
                    VALUES ('{placa_veiculo}', '{id_estacionamento}')"""
        self.connection.insert_into_table(query)
        
    def read_veiculos(self):
        query = f"""SELECT * FROM veiculo"""
        result = self.connection.select_from_table(query)
        return result
    
    def read_codigo_de_barra(self, placa_veiculo):
        query = f"""SELECT dono_do_veiculo FROM veiculo WHERE placa_veiculo = '{placa_veiculo}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]
    
    def update_veiculo(self, placa_veiculo, nova_placa,modelo_veiculo, codigo_de_barra_dono, id_estacionamento):
        query = f"""UPDATE veiculo SET modelo_veiculo = '{modelo_veiculo}', dono_do_veiculo = '{codigo_de_barra_dono}', placa_veiculo = '{nova_placa}', estacionamento_id_estacionamento = '{id_estacionamento}'
                    WHERE placa_veiculo = '{placa_veiculo}'"""
        self.connection.update_table(query)
        query = f"""UPDATE estac_veic SET estacionamentos_id_estacionamento = '{id_estacionamento}', veiculo_placa_veiculo = '{nova_placa}'
                    WHERE veiculo_placa_veiculo = '{placa_veiculo}'"""
        self.connection.update_table(query)

        
    def deletar_veiculo(self, placa_veiculo):
        query = f"""DELETE FROM estac_veic WHERE veiculo_placa_veiculo = '{placa_veiculo}'"""
        self.connection.delete_from_table(query)
        
        query = f"""DELETE FROM veiculo WHERE placa_veiculo = '{placa_veiculo}'"""
        self.connection.delete_from_table(query)
        
        
    def close_connection(self):
        self.connection.close_connection()
        

class gerencia_estacionamento():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_estacionamento(self, id_estacionamento, nome_estacionamento):
        query = f"""INSERT INTO estacionamentos (id_estacionamento, nome_estacionamento)
                    VALUES ('{id_estacionamento}', '{nome_estacionamento}')"""
        self.connection.insert_into_table(query)
        
    def read_estacionamento(self):
        query = f"""SELECT * FROM estacionamentos"""
        result = self.connection.select_from_table(query)
        return result
    
    def update_estacionamento(self, id_estacionamento, nome_estacionamento):
        query = f"""UPDATE estacionamentos SET nome_estacionamento = '{nome_estacionamento}'
                    WHERE id_estacionamento = '{id_estacionamento}'"""
        self.connection.update_table(query)
        
    def deletar_estacionamento(self, id_estacionamento):
        query = f"""DELETE FROM estacionamentos WHERE id_estacionamento = '{id_estacionamento}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()

class gerencia_estac_veic():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_estac_veic(self, veiculo_placa_veiculo, estacionamentos_id_estacionamento, data_hora_entrada):
        query = f"""INSERT INTO estac_veic (veiculo_placa_veiculo, estacionamentos_id_estacionamento, data_hora_entrada)
                    VALUES ('{veiculo_placa_veiculo}', '{estacionamentos_id_estacionamento}, '{data_hora_entrada}')"""
        self.connection.insert_into_table(query)
        
    def read_estac_veic(self):
        query = f"""SELECT * FROM estac_veic"""
        result = self.connection.select_from_table(query)
        return result
    
    def read_data_hora_entrada(self, veiculo_placa_veiculo):
        query = f"""SELECT data_hora_entrada FROM estac_veic WHERE veiculo_placa_veiculo = '{veiculo_placa_veiculo}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]
    
    def update_estac_veic(self, veiculo_placa_veiculo, estacionamentos_id_estacionamento):
        query = f"""UPDATE estac_veic SET estacionamentos_id_estacionamento = '{estacionamentos_id_estacionamento}'
                    WHERE veiculo_placa_veiculo = '{veiculo_placa_veiculo}'"""
        self.connection.update_table(query)
        
    def deletar_estac_veic(self, veiculo_placa_veiculo):
        query = f"""DELETE FROM estac_veic WHERE veiculo_placa_veiculo = '{veiculo_placa_veiculo}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()
        

class gerencia_historico():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = connect_sql(host_name, user_name, user_password, database_name)
        
    def criar_historico(self, veiculo_placa_veiculo, estacionamentos_id_estacionamento, data_hora_entrada, data_hora_saida):
        query = f"""INSERT INTO historico (veiculo_placa_veiculo, estacionamentos_id_estacionamento, data_hora_entrada, data_hora_saida)
                    VALUES ('{veiculo_placa_veiculo}', '{estacionamentos_id_estacionamento}', '{data_hora_entrada}', '{data_hora_saida}')"""
        self.connection.insert_into_table(query)
        
    def read_historico(self):
        query = f"""SELECT * FROM historico"""
        result = self.connection.select_from_table(query)
        return result
    
    def update_historico(self, veiculo_placa_veiculo, estacionamentos_id_estacionamento, data_hora_entrada, data_hora_saida):
        query = f"""UPDATE historico SET estacionamentos_id_estacionamento = '{estacionamentos_id_estacionamento}', data_hora_entrada = '{data_hora_entrada}', data_hora_saida = '{data_hora_saida}'
                    WHERE veiculo_placa_veiculo = '{veiculo_placa_veiculo}'"""
        self.connection.update_table(query)
        
    def deletar_historico(self, veiculo_placa_veiculo):
        query = f"""DELETE FROM historico WHERE veiculo_placa_veiculo = '{veiculo_placa_veiculo}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()
        





        
    
            
        
    
            