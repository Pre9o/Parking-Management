from sql_manager import sql_manager

class gerencia_veiculos():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
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