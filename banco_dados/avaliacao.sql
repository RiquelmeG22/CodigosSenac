create database avaliacao;
use avaliacao;

create table religiao (
id_religiao int PRIMARY key AUTO_INCREMENT,
nome varchar(100)
);
create table raca (
id_raca int PRIMARY key AUTO_INCREMENT,
nome varchar(100),
carcteristicas text
);

create table genero (
id_genero int PRIMARY key AUTO_INCREMENT,
nome varchar(50)
);

create table estado (
id_estado int PRIMARY key AUTO_INCREMENT,
nome varchar(50)
);

create table cidade (
id_cidade int PRIMARY key AUTO_INCREMENT,
nome varchar(50)
);

create table endereco (
id_endereco int PRIMARY key AUTO_INCREMENT,
rua varchar(50),
numero VARCHAR(10),
bairro varchar(60),
cep varchar(20) not null
);


create table agencia (
id_agencia int PRIMARY key AUTO_INCREMENT,
numero_agencia VARCHAR(20) NOT null unique,
id_cidade int,
id_estado int,
id_endereco int,
Foreign Key (id_cidade) REFERENCES cidade (id_cidade),
Foreign Key (id_estado) REFERENCES estado (id_estado),
Foreign Key (id_endereco) REFERENCES endereco (id_endereco)
);

create table estado_civil (
id_estado_civil int primary key AUTO_INCREMENT,
tipo VARCHAR(50)
);

create table deposito (
id_deposito int PRIMARY key AUTO_INCREMENT,
valor_deposito decimal,
id_agencia int,
id_cliente int,
Foreign Key (id_agencia) REFERENCES agencia (id_agencia),
Foreign Key (id_cliente) REFERENCES cliente (id_cliente)
);


create table saque (
id_saque int PRIMARY key AUTO_INCREMENT,
id_agencia int,
data_operacao date,
valor decimal,
numero_conta varchar(20),
Foreign Key (numero_conta) REFERENCES cliente (numero_conta),
Foreign Key (id_agencia) REFERENCES agencia (id_agencia)
);

create table cliente (
id_cliente int PRIMARY key AUTO_INCREMENT,
nome varchar(70),
cpf varchar(12) not null unique,
rg varchar(12) not null,
data_nascimento date,
fone varchar(20),
saldo decimal,
numero_conta varchar(20) UNIQUE not null,
id_endereco int,
id_estado int,
id_cidade int, 
id_genero int,
id_raca int,
id_religiao int,
id_estado_civil int,
id_agencia int,
Foreign Key (id_endereco) REFERENCES endereco (id_endereco),
Foreign Key (id_estado) REFERENCES estado (id_estado),
Foreign Key (id_cidade) REFERENCES cidade (id_cidade),
Foreign Key (id_genero) REFERENCES genero (id_genero),
Foreign Key (id_raca) REFERENCES raca (id_raca),
Foreign Key (id_religiao) REFERENCES religiao (id_religiao),
Foreign Key (id_estado_civil) REFERENCES estado_civil (id_estado_civil),
Foreign Key (id_agencia) REFERENCES agencia (id_agencia)
);

INSERT INTO religiao (nome) VALUES ('Cristianismo');

INSERT INTO raca (nome, carcteristicas) VALUES ('Caucasiano', 'Pele clara, cabelo liso ou ondulado');

INSERT INTO genero (nome) VALUES ('Masculino');

INSERT INTO estado (nome) VALUES ('São Paulo');

INSERT INTO cidade (nome) VALUES ('Guarulhos');

INSERT INTO endereco (rua, numero, bairro, cep) VALUES ('Avenida Paulista', '1578', 'Bela Vista', '01310-200');

INSERT INTO agencia (numero_agencia, id_cidade, id_estado, id_endereco) VALUES ('1234', 1, 1, 1);

INSERT INTO estado_civil (tipo) VALUES ('Solteiro');

INSERT INTO cliente (nome, cpf, rg, data_nascimento, fone, saldo, numero_conta, id_endereco, id_estado, id_cidade, id_genero, id_raca, id_religiao, id_estado_civil, id_agencia) VALUES 
('João Silva', '12345678901', 'MG1234567', '1990-01-01', '11987654321', 1000.00, '00112233', 1, 1, 1, 1, 1, 1, 1, 1);

INSERT INTO deposito (valor_deposito, id_agencia, id_cliente) VALUES (500.00, 1, 1);

INSERT INTO saque (id_agencia, data_operacao, valor, numero_conta) VALUES (1, '2024-09-23', 200.00, '00112233');

select * from cliente;

select * from saque;

describe cliente;

ALTER TABLE deposito ADD COLUMN numero_conta VARCHAR(20);


DELIMITER $

create trigger trg_saque after 
insert on saque for each row begin
update cliente set saldo = saldo - NEW.numero_conta;
end; $

create trigger trg_deposito
after insert ON deposito
FOR EACH ROW
BEGIN
    UPDATE cliente
    SET saldo = saldo + NEW.valor_deposito
    WHERE numero_conta = NEW.numero_conta;
END; $

DELIMITER ;



