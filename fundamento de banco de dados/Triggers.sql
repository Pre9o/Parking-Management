DELIMITER //

CREATE TRIGGER after_delete_veiculo_estacionado
AFTER DELETE ON veiculo_estacionado
FOR EACH ROW
BEGIN
    DECLARE placa_veiculo VARCHAR(45);
    DECLARE id_estacionamento INT;
    DECLARE data_hora_entrada DATETIME;
    DECLARE data_hora_saida DATETIME;

    -- Obter informações do veículo estacionado excluído
    SET placa_veiculo = OLD.placa_veiculo_estacionado;
    SET id_estacionamento = OLD.estacionamentos_id_estacionamento;
    SET data_hora_entrada = OLD.data_entrada;

    -- Obter data e hora atual para a saída
    SET data_hora_saida = NOW();

    -- Verificar se já existe um registro para este veículo e estacionamento
    IF EXISTS (SELECT 1 FROM historico WHERE placa_veiculo = placa_veiculo AND estacionamentos_id_estacionamento = id_estacionamento) THEN
        -- Atualizar o registro existente
        UPDATE historico
        SET data_saida = data_hora_saida
        WHERE placa_veiculo = placa_veiculo AND estacionamentos_id_estacionamento = id_estacionamento;
    ELSE
        -- Criar um novo registro no histórico
        INSERT INTO historico (placa_veiculo, estacionamentos_id_estacionamento, data_entrada, data_saida)
        VALUES (placa_veiculo, id_estacionamento, data_hora_entrada, data_hora_saida);
    END IF;
END;
//

DELIMITER ;