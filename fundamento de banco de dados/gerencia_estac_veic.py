from sql_manager import sql_manager

class gerencia_estac_veic():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
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