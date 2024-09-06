create database sprint;
use sprint;

create table atleta (
id_Atleta int primary key auto_increment,
nome varchar(40),
modalidade varchar(40),
qtdMedalha int
);

INSERT INTO atleta (nome, modalidade, qtdMedalha) 
VALUES 
('Ana Silva', 'Atletismo', 3),
('João Souza', 'Atletismo', 1),
('Maria Fernandes', 'Natação', 2),
('Carlos Oliveira', 'Natação', 5),
('Lucas Pereira', 'Ginástica', 4),
('Roberto Santos', 'Ginástica', 1);

select * from atleta;

update atleta set qtdMedalha = '5' where id_Atleta = 1;

update atleta set qtdMedalha = '9' where id_Atleta = 2 or id_Atleta = 3;

update atleta set nome = "Riquelme Gomes" where id_Atleta = 4;

alter table atleta add column dtNasc date;

update atleta set dtNasc = (current_date());
SET SQL_SAFE_UPDATES = 0;

delete from atleta where id_Atleta = 5;

SELECT * FROM atleta WHERE modalidade <> 'Natação';

select * from atleta where qtdMedalha >= 3;

alter table atleta modify column modalidade varchar(60);

describe atleta;

truncate atleta;

