create database cadastro;

use cadastro;

create table cadSenac (
Idcadastro int primary key auto_increment,
usuaro varchar(50) unique,
senha varchar(40),
configSenha varchar(40)
);



insert into cadSenac (Idcadastro, usuario, senha) values
('1', 'rique', 'senha',);

select * from cadSenac;