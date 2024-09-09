create database sprint;
use sprint;

create table filme (
idFilme int primary key auto_increment,
titulo varchar(50),
genero varchar(40),
diretor varchar(40)
);


INSERT INTO filme (idFilme, titulo, genero, diretor) VALUES
(1, 'O Senhor dos Anéis: A Sociedade do Anel', 'Fantasia', 'Peter Jackson'),
(2, 'O Senhor dos Anéis: As Duas Torres', 'Fantasia', 'Peter Jackson'),
(3, 'O Senhor dos Anéis: O Retorno do Rei', 'Fantasia', 'Peter Jackson'),
(4, 'Jurassic Park', 'Aventura', 'Steven Spielberg'),
(5, 'E.T. - O Extraterrestre', 'Aventura', 'Steven Spielberg'),
(6, 'A Lista de Schindler', 'Drama', 'Steven Spielberg'),
(7, 'Minority Report', 'Ficção Científica', 'Steven Spielberg');

select * from filme;
alter table filme add protagonista varchar(50);
update filme set protagonista = 'Riquelme Gomes';
SET SQL_SAFE_UPDATES = 0;
alter table filme modify column diretor varchar(150);
update filme set diretor = 'Yuri Ferreira' where idFilme = 5;
update filme set diretor = 'Alcir Junior' where idFilme = 2 or idFilme = 7;
update filme set titulo = 'Flamengo' where idFilme = 6;
delete  from filme where idFilme = 3;
SELECT * FROM atleta WHERE modalidade <> 'Natação';

select * from filme where genero <> 'Drama';

select * from filme where genero = 'Suspense';

describe filme;

truncate filme;

