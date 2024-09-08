create database sprint;
use sprint;

create table professor (
idProfessor int primary key auto_increment,
nome varchar(50),
especialidade varchar(40),
dtNasc date
);

INSERT INTO Professor (idProfessor, nome, especialidade, dtNasc) VALUES
(1, 'Carlos Silva', 'Matemática', '1983-10-13'),
(2, 'Maria Oliveira', 'Física', '1975-08-22'),
(3, 'João Santos', 'Matemática', '1990-03-15'),
(4, 'Ana Costa', 'Química', '1980-11-30'),
(5, 'Pedro Almeida', 'Física', '1986-06-25'),
(6, 'Cláudia Martins', 'Biologia', '1992-09-05');

select * from professor;

alter table professor add funcao varchar(50) check (funcao in ('monitor', 'assistente', 'titular'));

update Professor set funcao = 'titular' where idProfessor in (1, 2, 3, 4, 5, 6);


insert into professor (idProfessor, nome, especialidade, dtNasc, funcao) 
values (7, 'Fernanda Lima', 'Matemática', '1985-12-01', 'titular');

delete from professor where idProfessor = 5;

select nome from professor where funcao = 'titular';

select especialidade, dtNasc from professor  where funcao = 'monitor';

update professor set dtNasc = '1985-03-15' where idProfessor = 3;

truncate professor;

