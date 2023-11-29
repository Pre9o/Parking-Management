from gerencia_usuarios import *
from gerencia_veiculos import *
from gerencia_atribuicao import *
from gerencia_estacionamento import *
from adicoes import *

class verificacoes():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
    
    def verificacao(host_name, user_name, user_password, database_name, verifica, tipo):
        if tipo == "usuario":
            verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(verifica)
            
            while verifica == None:
                print("Usuário não encontrado!")
                verifica = input("Digite o código de barra do usuário: ")
                verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(verifica)
            
            return verifica
        
        elif tipo == "veiculo":
            verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(verifica)

            while verifica == None:
                print("Usuário não encontrado!")
                print("1- Digitar novamente o código do dono: ")
                print("2- Criar um novo usuário")
                option = input("Digite a opção desejada: ")
                if option == "1":
                    usuario = input("Digite o codigo do dono: ")
                    verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(usuario)
                elif option == "2":
                    usuario = adicoes.adicionar_usuario(True)
                    verifica = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(usuario)
            
            return verifica
        
        elif tipo == "atribuicao":
            while verifica == None:
                print("Atribuição não encontrada!")
                atribuicao = input("Digite o nome da atribuição: ").capitalize()
                verifica = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
            
            return verifica
        
        elif tipo == "estacionamento":
            while verifica == None:
                print("Estacionamento não encontrado!")
                id_estacionamento = input("Digite o id do estacionamento: ")
                verifica = gerencia_estacionamento(host_name, user_name, user_password, database_name).get_estacionamento(id_estacionamento)
            
            return verifica
        
        elif tipo == "placa":
            verifica = gerencia_veiculos(host_name, user_name, user_password, database_name).get_placa(verifica)
            while verifica == None:
                print("Veículo não encontrado!")
                placa = input("Digite a placa do veículo: ").upper()
                verifica = gerencia_veiculos(host_name, user_name, user_password, database_name).get_placa(placa)
            
            return verifica
