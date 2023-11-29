from gerencia_usuarios import gerencia_usuarios
from gerencia_veiculos import gerencia_veiculos
from gerencia_atribuicao import gerencia_atribuicao
from gerencia_estacionamento import gerencia_estacionamento

class remocoes():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name

    def remover_usuario(host_name, user_name, user_password, database_name):
        codigo_de_barra = input("Digite o código de barra do usuário que quer remover: ")
        verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
        
        while verificacao_codigo == None:
            print("Usuário não encontrado!")
            codigo_de_barra = input("Digite o código de barra do usuário que quer remover: ")
            verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
            
        gerencia_usuarios(host_name, user_name, user_password, database_name).deletar_usuario(codigo_de_barra)
        
        print("Usuário removido com sucesso!")

    def remover_veiculo(host_name, user_name, user_password, database_name):
        placa = input("Digite a placa do veículo que quer remover: ").upper()
        gerencia_veiculos(host_name, user_name, user_password, database_name).deletar_veiculo(placa)
        
        print("Veículo removido com sucesso!")

    def remover_atribuicao(host_name, user_name, user_password, database_name):
        id_atribuicao = input("Digite o id da atribuição que quer remover: ")
        gerencia_atribuicao(host_name, user_name, user_password, database_name).deletar_atribuicao(id_atribuicao)
        
        print("Atribuição removida com sucesso!")

    def remover_estacionamento(host_name, user_name, user_password, database_name):
        id_estacionamento = input("Digite o id do estacionamento que quer remover: ")
        gerencia_estacionamento(host_name, user_name, user_password, database_name).deletar_estacionamento(id_estacionamento)
        
        print("Estacionamento removido com sucesso!")