from sql_manager import sql_manager

class gerencia_historico():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
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