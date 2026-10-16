CREATE DATABASE OrcamentoPessoal;
USE OrcamentoPessoal;

DROP TABLE USUARIOS;

CREATE TABLE USUARIOS(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45),
    email VARCHAR(45),
    palavra_passe VARCHAR(45),
    PRIMARY KEY(id)
);

CREATE TABLE CONTA(
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER,
    saldo_atual REAL,
    PRIMARY KEY(id),
    Foreign Key (id_usuario) REFERENCES USUARIOS(id)
);

CREATE TABLE CATEGORIAS(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(90),
    icone VARCHAR(120),
    PRIMARY KEY(id)
);

CREATE TABLE TRANSACOES(
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER,
    id_conta INTEGER,
    tipo ENUM('Concluído', 'Pendente', 'Cancelado'),
    id_categoria INTEGER,
    valor REAL,
    descricao VARCHAR(45),
    data_transacao DATE,
    PRIMARY KEY(id),
    Foreign Key (id_usuario) REFERENCES USUARIOS(id),
    Foreign Key (id_categoria) REFERENCES CATEGORIAS(id),
    Foreign key (id_conta) REFERENCES CONTA(id)
);

CREATE TABLE OBJETIVOS(
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER,
    nome VARCHAR(45),
    valor_meta REAL,
    valor_atual REAL,
    data_limite DATE,
    PRIMARY KEY(id),
    Foreign Key (id_usuario) REFERENCES USUARIOS(id)
);

INSERT INTO orcamentopessoal.usuarios VALUES
(DEFAULT, 'Kem', 'Kem117@gmail.com', '1234');

INSERT INTO orcamentopessoal.usuarios VALUES
(DEFAULT, 'Jason', 'JasonMoreira79@icloud.com', '1112');

INSERT INTO orcamentopessoal.usuarios VALUES
(DEFAULT, 'Eunice', 'EuniceAlmeida7911@outlook.com', '1123');

-- USE orcamentopessoal;
-- ALTER TABLE TRANSACOES ADD id_conta INT AFTER id_usuario;
-- ALTER TABLE TRANSACOES ADD Foreign Key (id_conta) REFERENCES CONTA(id);


-- SELECT * FROM CONTA;