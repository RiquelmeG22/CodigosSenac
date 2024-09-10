create database login;

use login;

create table login (
IdLogin int primary key auto_increment,
usuario varchar(50) unique,
senha varchar(40),
texto text
);

describe login; 

insert into login (IdLogin, usuario, senha, texto) values
('1', 'Riq10', 'Senha231', 'GG');

select * from login;