CREATE VIEW `estacionamento`.`vw_usuarios_atribuicoes_veiculos` AS
    SELECT 
        `u`.`nome_usuario` AS `nome_usuario`,
        `u`.`codigo_de_barra` AS `codigo_de_barra`,
        `u`.`atribuicao_id_atribuicao` AS `atribuicao_id_atribuicao`,
        `a`.`nome_atribuicao` AS `nome_atribuicao`,
        `v`.`placa_veiculo` AS `placa_veiculo`,
        `v`.`modelo_veiculo` AS `modelo_veiculo`,
        `v`.`dono_do_veiculo` AS `dono_do_veiculo`
    FROM
        ((`estacionamento`.`usuario` `u`
        LEFT JOIN `estacionamento`.`atribuicao` `a` ON ((`u`.`atribuicao_id_atribuicao` = `a`.`id_atribuicao`)))
        LEFT JOIN `estacionamento`.`veiculo` `v` ON ((`u`.`codigo_de_barra` = `v`.`dono_do_veiculo`)))