create database EAoQuadrado;
use EAoQuadrado;

create table cargo (
id_cargo int primary key auto_increment,
cargo varchar(100) not null
);

create table permissao (
id_permissao int primary key auto_increment,
permissao varchar(100)
);

create table administrador (
id_adm int primary key auto_increment,
nome_usario varchar(100) not null,
email varchar(100) unique not null,
senha_adm varchar(100) not null,
nome_adm varchar(100) not null,
sobrenome_adm varchar(50) not null,
cargo varchar(50) not null,
data_nascimento date not null,
cpf varchar(11) unique not null
);



