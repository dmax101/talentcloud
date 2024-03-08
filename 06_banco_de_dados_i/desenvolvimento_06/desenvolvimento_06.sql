-- Criando o banco de dados ESCOLA
CREATE DATABASE ESCOLA;

-- Utilizando o banco de dados ESCOLA
USE ESCOLA;

-- Criando a tabela ALUNO
CREATE TABLE ALUNO (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    endereco VARCHAR(255)
);

-- Inserindo um novo aluno na tabela ALUNO
INSERT INTO ALUNO (nome, email, endereco) VALUES ('João Silva', 'joao@example.com', 'Rua A, 123');

-- Inserindo outro aluno na tabela ALUNO
INSERT INTO ALUNO (nome, email, endereco) VALUES ('Maria Souza', 'maria@example.com', 'Avenida B, 456');
