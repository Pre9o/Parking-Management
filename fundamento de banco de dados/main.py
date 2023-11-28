import mysql.connector
from datetime import datetime
from mysql.connector import Error
from create_database_for_estacionamento import *
from create_tables_for_estacionamento import *
from gerencia_estacionamento import *
from gerencia_atribuicao import *
from gerencia_veiculos import *
from gerencia_usuarios import *
from gerencia_veiculo_estacionado import *
from gerencia_historico import *

# REFACTORING: Extract Method
# TO DO: Extract Method

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"

def entrada_veiculo(host_name, user_name, user_password, database_name):
    placa = input("Digite a placa do veículo: ").upper()
    placa = verificacao(placa,"placa")
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
        
    gerencia_historico(host_name, user_name, user_password, database_name).update_historico(placa, id_estacionamento, data_hora_entrada, data_hora_saida)


    gerencia_veiculo_estacionado(host_name, user_name, user_password, database_name).deletar_veiculo_estacionado(placa)
    
    print("Saída realizada com sucesso!") 
    

def menu_gerenciamento(host_name, user_name, user_password, database_name):
    while True:
                print("1 - Gerenciar usuários")
                print("2 - Gerenciar veículos")
                print("3 - Gerenciar atribuições")
                print("4 - Gerenciar estacionamentos")
                print("5 - Sair")

                option = input("Selecione a opção que você deseja gerenciar: ")

                if option == "1":
                    menu_usuarios(host_name, user_name, user_password, database_name)
                    
                elif option == "2":
                    menu_veiculos(host_name, user_name, user_password, database_name)

                elif option == "3":
                    menu_atribuicao(host_name, user_name, user_password, database_name)

                elif option == "4":
                    menu_estacionamento(host_name, user_name, user_password, database_name)

                elif option == "5":
                    break

                else:
                    print("Opção inválida!")
                    continue


def menu_vigilante(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Voltar")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            entrada_veiculo(host_name, user_name, user_password, database_name)

        elif opcao == 2:
            saida_veiculo(host_name, user_name, user_password, database_name)

        elif opcao == 3:
            break

        else:
            print("Opção inválida!")
            continue


def menu_usuarios(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Remover usuário")
        print("5 - Voltar")

        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            adicionar_usuario(host_name, user_name, user_password, database_name, False)
        
        elif opcao == 2:
            lista = gerencia_usuarios(host_name, user_name, user_password, database_name).read_usuarios()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_usuario(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_usuario(host_name, user_name, user_password, database_name)
        
        elif opcao == 5:
            break

        else:
            print("Opção inválida!")
            continue


def menu_veiculos(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Adicionar veículo")
        print("2 - Listar veículos")
        print("3 - Atualizar veículo")
        print("4 - Remover veículo")
        print("5 - Voltar")

        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            adicionar_veiculo(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_veiculos(host_name, user_name, user_password, database_name).read_veiculos()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_veiculo(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_veiculo(host_name, user_name, user_password, database_name)
        
        elif opcao == 5:
            break

        else:
            print("Opção inválida!")
            continue


def menu_atribuicao(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Adicionar atribuição")
        print("2 - Listar atribuições")
        print("3 - Atualizar atribuição")
        print("4 - Remover atribuição")
        print("5 - Voltar")

        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            adicionar_atribuicao(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_atribuicao(host_name, user_name, user_password, database_name).read_atribuicao()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_atribuicao(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_atribuicao(host_name, user_name, user_password, database_name)
        
        elif opcao == 5:
            break

        else:
            print("Opção inválida!")
            continue


def menu_estacionamento(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Adicionar estacionamento")
        print("2 - Listar estacionamentos")
        print("3 - Atualizar estacionamento")
        print("4 - Remover estacionamento")
        print("5 - Voltar")

        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            adicionar_estacionamento(host_name, user_name, user_password, database_name)
        
        elif opcao == 2:
            lista = gerencia_estacionamento(host_name, user_name, user_password, database_name).read_estacionamento()
            for i in lista:
                print(i)

        elif opcao == 3:
            atualizar_estacionamento(host_name, user_name, user_password, database_name)

        elif opcao == 4:
            remover_estacionamento(host_name, user_name, user_password, database_name)
        
        elif opcao == 5:
            break

        else:
            print("Opção inválida!")
            continue


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
    atribuicao = verificacao(atribuicao,"atribuicao")
    
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

    verificacao_usuario = verificacao(verificacao_usuario,"veiculo")
    
    gerencia_veiculos(host_name, user_name, user_password, database_name).criar_veiculo(placa, modelo, usuario)
    
    print("Veículo adicionado com sucesso!")


def verificacao(verifica, tipo):
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
                usuario = adicionar_usuario(host_name, user_name, user_password, database_name, True)
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







def adicionar_estacionamento(host_name, user_name, user_password, database_name):
    nome_estacionamento = input("Digite o nome do estacionamento: ")
    gerencia_estacionamento(host_name, user_name, user_password, database_name).criar_estacionamento(nome_estacionamento)
    
    print("Estacionamento adicionado com sucesso!")


def atualizar_usuario(host_name, user_name, user_password, database_name):
    codigo_de_barra = input("Digite o código de barra do usuário que quer atualizar: ")
    verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
    
    while verificacao_codigo == None:
        print("Usuário não encontrado!")
        codigo_de_barra = input("Digite o código de barra do usuário que quer atualizar: ")
        verificacao_codigo = gerencia_usuarios(host_name, user_name, user_password, database_name).get_usuario(codigo_de_barra)
    
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


def menu_principal(host_name, user_name, user_password, database_name):
    while True:
        print("1 - Menu de gerenciamento")
        print("2 - Menu do vigilante")
        print("3 - Sair")

        option = input("Selecione a opção que você deseja gerenciar: ")

        if option == "1":
            menu_gerenciamento(host_name, user_name, user_password, database_name)

        elif option == "2":
            menu_vigilante(host_name, user_name, user_password, database_name)

        elif option == "3":
            break
        
        else:
            print("Opção inválida!")
            continue
        


def main():
    while True:
        print("1 - Conectar ao banco de dados")
        print("2 - Criar banco de dados")
        print("3 - Iniciar o programa")
        print("4 - Sair")
        
        option = input("Selecione a opção que você deseja gerenciar: ")

        if option == "1":
            try:
                connection = mysql.connector.connect(host='localhost',
                                            database='estacionamento',
                                            user='root',
                                            password='totito12')
            
            except Error as e:
                print("Erro ao conectar ao banco de dados MySQL", e)
                
            

            if connection.is_connected():
                print('Conectado ao banco de dados MySQL')
                
            
        elif option == "2":
            create_database_for_estacionamento(host_name, user_name, user_password)
            create_tables_for_estacionamento(host_name, user_name, user_password, database_name)
            gerencia_atribuicao(host_name, user_name, user_password, database_name).criar_atribuicoes_padrao()
            gerencia_estacionamento(host_name, user_name, user_password, database_name).criar_estacionamentos_padrao()

        elif option == "3":
            menu_principal(host_name, user_name, user_password, database_name)
        
        elif option == "4":
            if (connection.is_connected()):
                connection.close()
            print("Conexão ao banco de dados MySQL encerrada")
            
            break
        
        else:
            print("Opção inválida!")
            continue
            
            
if __name__ == "__main__":
    main()
