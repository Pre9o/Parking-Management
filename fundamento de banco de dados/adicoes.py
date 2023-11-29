from gerencia_atribuicao import gerencia_atribuicao
from gerencia_usuarios import gerencia_usuarios
from gerencia_veiculos import gerencia_veiculos
from gerencia_estacionamento import gerencia_estacionamento
from verificacoes import verificacoes


class adicoes():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name

    def adicionar_atribuicao(host_name, user_name, user_password, database_name):
        nome_atribuicao = input("Digite o nome da atribuição: ").capitalize()
        id_atribuicao = input("Digite o id da atribuição: ")
        
        gerencia_atribuicao(host_name, user_name, user_password, database_name).criar_atribuicao(id_atribuicao, nome_atribuicao)
        
        print("Atribuição adicionada com sucesso!")


    def adicionar_usuario(host_name, user_name, user_password, database_name, return_codigos_de_barra):
        nome = input("Digite o nome do usuário: ").capitalize()
        atribuicao = input("Digite o nome da atribuição do usuário: ")
        codigo_de_barra = gerencia_usuarios(host_name, user_name, user_password, database_name).get_codigos_de_barra()
        atribuicao = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
        atribuicao = verificacoes.verificacao(host_name, user_name, user_password, database_name, atribuicao, "atribuicao")
        
        gerencia_usuarios(host_name, user_name, user_password, database_name).criar_usuario(nome, atribuicao, codigo_de_barra)
        
        print("Usuário adicionado com sucesso!")
        
        if return_codigos_de_barra:
            return codigo_de_barra
        
        else:
            return None

                                
    def adicionar_veiculo(host_name, user_name, user_password, database_name):
        placa = input("Digite a placa do veículo: ").upper()
        modelo = input("Digite o modelo do veículo: ").capitalize()
        usuario = input("Digite o codigo do dono: ")

        usuario = verificacoes.verificacao(host_name, user_name, user_password, database_name, usuario, "usuario")
        
        gerencia_veiculos(host_name, user_name, user_password, database_name).criar_veiculo(placa, modelo, usuario)
        
        print("Veículo adicionado com sucesso!")

    def adicionar_estacionamento(host_name, user_name, user_password, database_name):
        nome_estacionamento = input("Digite o nome do estacionamento: ")
        gerencia_estacionamento(host_name, user_name, user_password, database_name).criar_estacionamento(nome_estacionamento)
        
        print("Estacionamento adicionado com sucesso!")