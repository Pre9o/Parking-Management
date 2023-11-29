from sql_manager import sql_manager

class gerencia_veiculo_estacionado():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
    def criar_veiculo_estacionado(self, placa_veiculo_estacionado, codigo_de_barra_usuario, estacionamentos_id_estacionamento, data_entrada):
        query = f"""INSERT INTO veiculo_estacionado (placa_veiculo_estacionado, codigo_de_barra_usuario ,estacionamentos_id_estacionamento, data_entrada)
                    VALUES ('{placa_veiculo_estacionado}', '{codigo_de_barra_usuario}' ,'{estacionamentos_id_estacionamento}', '{data_entrada}')"""
        self.connection.insert_into_table(query)
        
    def read_veiculo_estacionado(self):
        query = f"""SELECT * FROM veiculo_estacionado"""
        result = self.connection.select_from_table(query)
        return result
    
    def read_placa(self, codigo_de_barra_usuario):
        query = f"""SELECT placa_veiculo_estacionado FROM veiculo_estacionado WHERE codigo_de_barra_usuario = '{codigo_de_barra_usuario}'"""
        result = self.connection.execute_read_query(query)
        return result
        
    def read_data_entrada(self, placa_veiculo_estacionado):
        query = f"""SELECT data_entrada FROM veiculo_estacionado WHERE placa_veiculo_estacionado = '{placa_veiculo_estacionado}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]

    def get_id_estacionamento(self, placa_veiculo_estacionado):
        query = f"""SELECT estacionamentos_id_estacionamento FROM veiculo_estacionado WHERE placa_veiculo_estacionado = '{placa_veiculo_estacionado}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]

    def update_veiculo_estacionado(self, placa_veiculo_estacionado, estacionamentos_id_estacionamento):
        query = f"""UPDATE veiculo_estacionado SET estacionamentos_id_estacionamento = '{estacionamentos_id_estacionamento}'
                    WHERE placa_veiculo_estacionado = '{placa_veiculo_estacionado}'"""
        self.connection.update_table(query)
        
    def deletar_veiculo_estacionado(self, placa_veiculo_estacionado):
        query = f"""DELETE FROM veiculo_estacionado WHERE placa_veiculo_estacionado = '{placa_veiculo_estacionado}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()