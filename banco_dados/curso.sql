create database sprint;
use sprint;

create table curso (
idCurso int primary key auto_increment,
nome varchar(50),
sigla varchar(3),
cordenador varchar(20)
);

INSERT INTO curso (idCurso, nome, sigla, cordenador) VALUES
('1', 'Ciência da Computação', 'CC', 'Dr. Ana Costa'),
('2', 'Engenharia Elétrica', 'EE', 'Prof. Carlos Silva'),
('3', 'Matemática', 'MAT', 'Prof. João Santos');

select * FROM curso;
select cordenador from curso;

select * from curso where sigla = 'EE';

select * from curso order by nome;

select * from curso order by cordenador desc;

select * from curso where nome like  'E%';
 
select * from curso where nome like  '%a';
  
select * from curso where nome like  '%c_';

truncate curso;
