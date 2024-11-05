-- Criando o banco de dados 'gerenciamento' e definindo como default
CREATE DATABASE gerenciamento;
USE gerenciamento;


-- Criando a tabela 'usuario'
CREATE TABLE `usuario` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`nome` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL UNIQUE,
    `senha` VARCHAR(255) NOT NULL,
	`cargo` ENUM('CONSTRUTOR', 'MARKETING', 'LOGISTICA', 'GERENTE', 'TI') NOT NULL,
	`tipo` ENUM('ADMINISTRADOR', 'SUPERVISOR', 'COLABORADOR') NOT NULL,
	`foto` VARCHAR(255),
	`data_admissao` DATETIME NOT NULL,
	PRIMARY KEY(`id`)
);


-- Criando a tabela 'equipamento'
CREATE TABLE `equipamento` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`nome` VARCHAR(255) NOT NULL,
	`categoria` ENUM('PROTECAO_OCULAR_E_FACIAL', 'PROTECAO_MAOS_E_BRACOS', 'PROTECAO_CONTRA_QUEDA', 'PROTECAO_RESPIRATORIA', 'PROTECAO_PES_E_PERNAS', 'PROTECAO_AUDITIVA') NOT NULL,
	`quantidade_total` INTEGER NOT NULL,
	`validade` DATE NOT NULL,
	PRIMARY KEY(`id`)
);


-- Criando a tabela 'emprestimo'
CREATE TABLE `emprestimo` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`quantidade` INTEGER NOT NULL,
	`status` ENUM('EMPRESTADO', 'EM_USO', 'FORNECIDO') NOT NULL,
	`data_emprestimo` DATETIME NOT NULL,
	`data_devolucao_prevista` DATETIME NOT NULL,
	`id_usuario` INTEGER NOT NULL,
	`id_equipamento` INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);


-- Criando a tabela 'historico'
CREATE TABLE `historico` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`quantidade` INTEGER NOT NULL,
	`status` ENUM('DEVOLVIDO', 'DANIFICADO', 'PERDIDO') NOT NULL,
	`observacao` TEXT(65535) NOT NULL,
	`data_emprestimo` DATETIME NOT NULL,
	`data_devolucao_efetiva` DATETIME,
	`nome_equipamento` VARCHAR(255) NOT NULL,
	`nome_usuario` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id`)
);


-- Adicionando a chave estrângeira 'id_usuario'
ALTER TABLE `emprestimo`
	ADD FOREIGN KEY(`id_usuario`) REFERENCES `usuario`(`id`) ON UPDATE NO ACTION ON DELETE NO ACTION;


-- Adicionando a chave estrângeira 'id_equipamento'
ALTER TABLE `emprestimo`
	ADD FOREIGN KEY(`id_equipamento`) REFERENCES `equipamento`(`id`) ON UPDATE NO ACTION ON DELETE NO ACTION;


-- Inserindo dados na tabela `usuario`
INSERT INTO `usuario` (`nome`, `email`, `cargo`, `tipo`, `foto`, `data_admissao`, `senha`) VALUES
('Administrador', 'administrador@example.com', 'TI', 'ADMINISTRADOR', 'usuarios/exemplos/exemplo-1.jpg', '2024-12-12 12:00:00', '123456'),
('Supervisor', 'supervisor@example.com', 'GERENTE', 'SUPERVISOR', 'usuarios/exemplos/exemplo-2.jpg', '2024-12-12 12:00:00', '123456'),
('Colaborador', 'colaborador@example.com', 'CONSTRUTOR', 'COLABORADOR', 'usuarios/exemplos/exemplo-1.jpg', '2024-12-12 12:00:00', '123456');


-- Inserindo dados na tabela `equipamento`
INSERT INTO `equipamento` (`nome`, `categoria`, `quantidade_total`, `validade`) VALUES
('Óculos de Proteção', 'PROTECAO_OCULAR_E_FACIAL', 50, '2026-12-12'),
('Luvas de Segurança', 'PROTECAO_MAOS_E_BRACOS', 100, '2026-12-12'),
('Capacete de Segurança', 'PROTECAO_CONTRA_QUEDA', 75, '2026-12-12');


-- Inserindo dados na tabela `emprestimo`
INSERT INTO `emprestimo` (`quantidade`, `status`, `data_emprestimo`, `data_devolucao_prevista`, `id_usuario`, `id_equipamento`) VALUES
(25, 'EMPRESTADO', '2024-12-12 12:00:00', '2024-12-12 12:00:00', 2, 1),
(2, 'EM_USO', '2024-12-12 12:00:00', '2024-12-12 12:00:00', 3, 2),
(1, 'FORNECIDO', '2024-12-12 12:00:00', '2024-12-12 12:00:00', 3, 3);


-- Inserindo dados na tabela `historico`
INSERT INTO `historico` (`quantidade`, `status`, `observacao`, `data_emprestimo`, `data_devolucao_efetiva`, `nome_equipamento`, `nome_usuario`) VALUES
(50, 'DEVOLVIDO', 'Equipamento devolvido em boas condições.', '2024-12-12 12:00:00', '2024-12-12 12:00:00', 'Óculos de Proteção', 'Supervisor'),
(2, 'DANIFICADO', 'Equipamento apresentou desgaste durante o uso.', '2024-12-12 12:00:00', '2024-12-12 12:00:00', 'Luvas de Segurança', 'Colaborador'),
(1, 'PERDIDO', 'Equipamento não foi devolvido no prazo.', '2024-12-12 12:00:00', NULL, 'Capacete de Segurança', 'Colaborador');
