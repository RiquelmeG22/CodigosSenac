create database sprint2;
use sprint2;

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

create table musica (
idMusica int primary key auto_increment,
titulo varchar(40),
artista varchar(40),
genero varchar(40)
);

INSERT INTO musica (titulo, artista, genero)
VALUES
('Song 1', 'Artist A', 'Pop'),
('Song 2', 'Artist A', 'Pop'),
('Song 3', 'Artist B', 'Rock'),
('Song 4', 'Artist B', 'Rock'),
('Song 5', 'Artist C', 'Jazz'),
('Song 6', 'Artist D', 'Jazz'),
('Song 7', 'Artist C', 'Jazz');

select * from musica; 

alter table musica add column curtidas int;

update musica set curtidas = 10;

alter table musica modify column artista varchar(80);

update musica set curtidas = '5' where idMusica = 1;

update musica set curtidas = '6' where idMusica = 2 or idMusica = 3;

update musica set titulo = 'Baile do Corte 8' where idMusica = 5;

delete from musica where idMusica = 4;

SELECT * FROM musica WHERE genero <> 'funk';

select * from musica where curtidas >=20;

describe musica;





