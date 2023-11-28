from sql_manager import sql_manager

class gerencia_estacionamento():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
    def criar_estacionamento(self, nome_estacionamento):
        query = f"""INSERT INTO estacionamentos (nome_estacionamento)
                    VALUES ('{nome_estacionamento}')"""
        self.connection.insert_into_table(query)
        
    def criar_estacionamentos_padrao(self):
        query = f"""INSERT INTO estacionamentos (nome_estacionamento)
                    VALUES ('Estacionamento 1'), ('Estacionamento 2'), ('Estacionamento 3'), ('Estacionamento 4'), ('Estacionamento 5')"""
        self.connection.insert_into_table(query)
        
    def read_estacionamento(self):
        query = f"""SELECT * FROM estacionamentos"""
        result = self.connection.select_from_table(query)
        return result
    
    def update_estacionamento(self, nome_estacionamento):
        query = f"""UPDATE estacionamentos SET nome_estacionamento = '{nome_estacionamento}'"""
        self.connection.update_table(query)
        
    def deletar_estacionamento(self, id_estacionamento):
        query = f"""DELETE FROM estacionamentos WHERE id_estacionamento = '{id_estacionamento}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()
