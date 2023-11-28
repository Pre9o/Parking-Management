from sql_manager import sql_manager
import random

class gerencia_usuarios():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
    def criar_usuario(self, nome_usuario, atribuicao_usuario, codigo_de_barra):
        query = f"""INSERT INTO usuario (nome_usuario, atribuicao_id_atribuicao, codigo_de_barra)
                    VALUES ('{nome_usuario}', '{atribuicao_usuario}', '{codigo_de_barra}')"""
        self.connection.insert_into_table(query)
        
    def read_usuarios(self):
        query = f"""SELECT * FROM usuario"""
        result = self.connection.select_from_table(query)
        return result        
    
    def get_usuario(self, codigo_de_barra):
        query = f"""SELECT nome_usuario FROM usuario 
                WHERE codigo_de_barra = '{codigo_de_barra}'"""
        result = self.connection.execute_read_query(query)
        if result:
            return result[0][0]  
        else:
            return None
    
    def get_codigos_de_barra(self):
        query = f"""SELECT codigo_de_barra FROM usuario"""
        result = self.connection.execute_read_query(query)
        
        codigo_gerado = random.randint(100000000000, 999999999999)
        
        while codigo_gerado in result:
            codigo_gerado = random.randint(100000000000, 999999999999)
        
        return codigo_gerado
    
    def get_cartao_especial(self):
       a = 0
    
    def update_usuario(self, nome_usuario, atribuicao_usuario, codigo_de_barra):
        query = f"""UPDATE usuario SET nome_usuario = '{nome_usuario}', atribuicao_id_atribuicao = '{atribuicao_usuario}'
                    WHERE codigo_de_barra = '{codigo_de_barra}'"""
        self.connection.update_table(query)
        
    def deletar_usuario(self, codigo_de_barra):
        query = f"""DELETE FROM usuario WHERE codigo_de_barra = '{codigo_de_barra}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()