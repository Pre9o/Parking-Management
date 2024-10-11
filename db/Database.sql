CREATE DATABASE estacionamento

CREATE TABLE atribuicao (
            id_atribuicao INT NOT NULL,
            nome_atribuicao VARCHAR(45) NOT NULL,
            PRIMARY KEY (id_atribuicao))

CREATE TABLE usuario (
            nome_usuario VARCHAR(45) NOT NULL,
            atribuicao_id_atribuicao INT NOT NULL,
            codigo_de_barra VARCHAR(45) NOT NULL,
            PRIMARY KEY (codigo_de_barra),
            FOREIGN KEY (atribuicao_id_atribuicao) REFERENCES atribuicao (id_atribuicao)
            )

CREATE TABLE veiculo (
            placa_veiculo VARCHAR(45) NOT NULL,
            modelo_veiculo VARCHAR(45) NOT NULL,
            dono_do_veiculo VARCHAR(45) NOT NULL,
            PRIMARY KEY (placa_veiculo),
            FOREIGN KEY (dono_do_veiculo) REFERENCES usuario (codigo_de_barra))

CREATE TABLE estacionamentos (
            id_estacionamento INT NOT NULL AUTO_INCREMENT,
            nome_estacionamento VARCHAR(45) NOT NULL,
            PRIMARY KEY (id_estacionamento))

CREATE TABLE veiculo_estacionado (
            id_veiculo_estacionado INT NOT NULL AUTO_INCREMENT,
            placa_veiculo_estacionado VARCHAR(45) NOT NULL,
            codigo_de_barra_usuario VARCHAR(45) NOT NULL,
            estacionamentos_id_estacionamento INT NOT NULL,
            data_hora_entrada DATETIME NOT NULL,
            PRIMARY KEY (id_veiculo_estacionado),
            FOREIGN KEY (placa_veiculo_estacionado) REFERENCES veiculo (placa_veiculo),
            FOREIGN KEY (codigo_de_barra_usuario) REFERENCES usuario (codigo_de_barra),
            FOREIGN KEY (estacionamentos_id_estacionamento) REFERENCES estacionamentos (id_estacionamento))

CREATE TABLE historico (
            id_historico INT NOT NULL AUTO_INCREMENT,
            placa_veiculo VARCHAR(45) NOT NULL,
            estacionamentos_id_estacionamento INT NOT NULL,
            data_entrada DATETIME NOT NULL,

            data_saida DATETIME,

            PRIMARY KEY (id_historico),
            FOREIGN KEY (placa_veiculo) REFERENCES veiculo (placa_veiculo),
            FOREIGN KEY (estacionamentos_id_estacionamento) REFERENCES estacionamentos (id_estacionamento))