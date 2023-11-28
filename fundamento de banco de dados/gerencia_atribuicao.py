from sql_manager import sql_manager

class gerencia_atribuicao():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = sql_manager(host_name, user_name, user_password, database_name)
        
    def criar_atribuicao(self, id_atribuicao, nome_atribuicao):
        query = f"""INSERT INTO atribuicao (id_atribuicao, nome_atribuicao)
                    VALUES ('{id_atribuicao}', '{nome_atribuicao}')"""
        self.connection.insert_into_table(query)
        
    def criar_atribuicoes_padrao(self):
        query = f"""INSERT INTO atribuicao (id_atribuicao, nome_atribuicao)
                    VALUES ('1', 'Professor'), ('2', 'Aluno'), ('3', 'Funcionário'), ('4', 'Visitante')"""
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
            return result[0][0]  
        else:
            return None  
    
    def update_atribuicao(self, nome_atribuicao, id_atribuicao):
        query = f"""UPDATE atribuicao SET nome_atribuicao = '{nome_atribuicao}'
                    WHERE id_atribuicao = '{id_atribuicao}'"""
        self.connection.update_table(query)
        
    def deletar_atribuicao(self, id_atribuicao):
        query = f"""DELETE FROM atribuicao WHERE id_atribuicao = '{id_atribuicao}'"""
        self.connection.delete_from_table(query)
        
    def close_connection(self):
        self.connection.close_connection()