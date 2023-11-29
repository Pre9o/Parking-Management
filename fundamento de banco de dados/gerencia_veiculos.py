from sql_manager import sql_manager

class gerencia_veiculos():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
    def criar_veiculo(self, placa_veiculo, modelo_veiculo, codigo_de_barra_dono):
        query = f"""INSERT INTO veiculo (placa_veiculo, modelo_veiculo, dono_do_veiculo)
                    VALUES ('{placa_veiculo}', '{modelo_veiculo}', '{codigo_de_barra_dono}')"""
        self.connection.insert_into_table(query)
        
    def read_veiculos(self):
        query = f"""SELECT * FROM veiculo"""
        result = self.connection.select_from_table(query)
        return result
    
    def get_placa(self, placa_veiculo):
        query = f"""SELECT placa_veiculo FROM veiculo WHERE placa_veiculo = '{placa_veiculo}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]
    
    def read_codigo_de_barra(self, placa_veiculo):
        query = f"""SELECT dono_do_veiculo FROM veiculo WHERE placa_veiculo = '{placa_veiculo}'"""
        result = self.connection.execute_read_query(query)
        return result[0][0]
    
    def update_veiculo(self, placa_veiculo, nova_placa,modelo_veiculo, codigo_de_barra_dono):
        query = f"""UPDATE veiculo SET modelo_veiculo = '{modelo_veiculo}', dono_do_veiculo = '{codigo_de_barra_dono}', placa_veiculo = '{nova_placa}'
                    WHERE placa_veiculo = '{placa_veiculo}'"""
        self.connection.update_table(query)
        query = f"""UPDATE veiculo_estacionado SET placa_veiculo_estacionado = '{nova_placa}'
                    WHERE placa_veiculo_estacionado = '{placa_veiculo}'"""

        self.connection.update_table(query)

    def deletar_veiculo(self, placa_veiculo):
        query = f"""DELETE FROM veiculo_estacionado WHERE placa_veiculo_estacionado = '{placa_veiculo}'"""

        self.connection.delete_from_table(query)
        
        query = f"""DELETE FROM veiculo WHERE placa_veiculo = '{placa_veiculo}'"""
        self.connection.delete_from_table(query)
        
        
    def close_connection(self):
        self.connection.close_connection()