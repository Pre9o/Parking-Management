from gerencia_usuarios import gerencia_usuarios
from gerencia_veiculos import gerencia_veiculos
from gerencia_atribuicao import gerencia_atribuicao
from gerencia_estacionamento import gerencia_estacionamento

class atualizacoes():
    def atualizar_usuario(host_name, user_name, user_password, database_name):
            codigo_de_barra = input("Digite o código de barra do usuário que quer atualizar: ")
            verificacao_codigo = gerencia_usuarios().get_usuario(codigo_de_barra)
            
            while verificacao_codigo == None:
                print("Usuário não encontrado!")
                codigo_de_barra = input("Digite o código de barra do usuário que quer atualizar: ")
                verificacao_codigo = gerencia_usuarios().get_usuario(codigo_de_barra)
            
            nome_usuario = input("Digite o novo nome do usuário: ").capitalize()
            
            atribuicao = input("Digite a nova atribuição do usuário: ").capitalize()
            atribuicao = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
            
            while atribuicao == None:
                print("Atribuição inválida!")
                atribuicao = input("Digite a nova atribuição do usuário: ").capitalize()
                atribuicao = gerencia_atribuicao(host_name, user_name, user_password, database_name).get_atribuicao(atribuicao)
            
            gerencia_usuarios(host_name, user_name, user_password, database_name).update_usuario(nome_usuario, atribuicao, codigo_de_barra)
            
            print("Usuário atualizado com sucesso!")

    def atualizar_veiculo(host_name, user_name, user_password, database_name):
        placa = input("Digite a placa do veículo que quer atualizar: ").upper()
        modelo = input("Digite o novo modelo do veículo: ").capitalize()
        dono_do_veiculo = input("Digite o novo dono do veículo: ").capitalize()
        nova_placa = input("Digite a nova placa do veículo: ").upper()
        gerencia_veiculos(host_name, user_name, user_password, database_name).update_veiculo(placa, nova_placa,modelo, dono_do_veiculo)
        
        print("Veículo atualizado com sucesso!")


    def atualizar_atribuicao(host_name, user_name, user_password, database_name):
        id_atribuicao = input("Digite o id da atribuição que quer atualizar: ")
        nome_atribuicao = input("Digite o novo nome da atribuição: ").capitalize()
        gerencia_atribuicao(host_name, user_name, user_password, database_name).update_atribuicao(nome_atribuicao, id_atribuicao)
        
        print("Atribuição atualizada com sucesso!")


    def atualizar_estacionamento(host_name, user_name, user_password, database_name):
        id_estacionamento = input("Digite o id do estacionamento que quer atualizar: ")
        novo_id_estacionamento = input("Digite o novo id do estacionamento: ")

        gerencia_estacionamento(host_name, user_name, user_password, database_name).update_estacionamento(id_estacionamento, novo_id_estacionamento)
        
        print("Estacionamento atualizado com sucesso!")
