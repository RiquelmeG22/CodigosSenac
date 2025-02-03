create database sprint2;
use sprint2;


create table revista (
idRevista int primary key auto_increment,
nome varchar(40),
categoria varchar(30)
);

INSERT INTO revista (idRevista, nome) VALUES 
('1', 'Revista A'),
('2', 'Revista B'),
('3', 'Revista C'),
('4', 'Revista D');


select * from revista;


UPDATE revista SET categoria = 'Ciência' WHERE idRevista = 1 or idRevista = 2 or idRevista = 3 or idRevista = 4;


INSERT INTO revista (idRevista, nome, categoria) VALUES 
('5', 'Revista E', 'Esportes'),
('6', 'Revista F', 'Saúde'),
('7', 'Revista G', 'Moda');

describe revista;

alter table revista modify column categoria varchar(40);
alter table revista add periodicidade varchar(15);

ALTER TABLE revista  DROP COLUMN periodicidade;
