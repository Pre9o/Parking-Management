from verificacoes import verificacoes
from gerencia_veiculos import gerencia_veiculos
from gerencia_veiculo_estacionado import gerencia_veiculo_estacionado
from gerencia_historico import gerencia_historico
from datetime import datetime

class vigilante():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name

    def entrada_veiculo(host_name, user_name, user_password, database_name):
        placa = input("Digite a placa do veículo: ").upper()
        placa = verificacoes.verificacao(host_name, user_name, user_password, database_name, placa, "placa")
        id_estacionamento = input("Digite o id do estacionamento: ")
        codigo_de_barra = gerencia_veiculos(host_name, user_name, user_password, database_name).read_codigo_de_barra(placa)

        while True:
            option = input("Quer utilizar a data e hora atual? (S/N): ").upper()
            if option == "S":
                data_hora_entrada = datetime.now()
                break
            elif option == "N":
                data = input("Digite a data: ")
                hora = input("Digite a hora: ")
                data_hora_entrada = data + " " + hora
                break
            else:
                print("Opção inválida!")
                continue

        gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).criar_veiculo_estacionado(placa, codigo_de_barra, id_estacionamento, data_hora_entrada)
        gerencia_historico(host_name, user_name, user_password, database_name).criar_historico(placa, id_estacionamento, data_hora_entrada, None)
        print("Entrada realizada com sucesso!")

       
    def saida_veiculo(host_name, user_name, user_password, database_name):
        placa = input("Digite a placa do veículo: ").upper()


        data_hora_entrada = gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).read_data_entrada(placa)
        id_estacionamento = gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).get_id_estacionamento(placa)


        while True:
            option = input("Quer utilizar a data e hora atual? (S/N): ").upper()
            if option == "S":
                data_hora_saida = datetime.now()
                break
            elif option == "N":
                data = input("Digite a data: ")
                hora = input("Digite a hora: ")
                data_hora_saida = data + " " + hora
                break
            else:
                print("Opção inválida!")
                continue
            
        # gerencia_historico().update_historico(placa, id_estacionamento, data_hora_entrada, data_hora_saida)


        gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).deletar_veiculo_estacionado(placa)
        
        print("Saída realizada com sucesso!") 
        

