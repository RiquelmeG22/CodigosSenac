create database login;

use login;

create table cadastro (
Idcadastro int primary key auto_increment,
usuario varchar(50) unique,
senha varchar(40),
texto text
);



insert into cadastro (Idcadastro, usuario, senha, texto) values
('1', 'rique', 'senha', 'GG');

select * from cadastro;