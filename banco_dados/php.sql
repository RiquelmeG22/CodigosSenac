create database php;
select * from php;
use php;


create table usuario (

id_usuario int auto_increment primary key,
nome varchar (50),
senha varchar (50),
setor varchar (50)

);

insert into usuario values (null, 'riquelme', 'rique10', 'usuario');
insert into usuario values (null, 'adminstrador', 'adm','admlocal');


create table cliente (

id_cliente int auto_increment primary key,
nome varchar(50),
sobrenome varchar(50),
endereco varchar(50),
email varchar(50),
sexo varchar(50)

);

insert into cliente values(null, 'jose', 'ramalho', 'florao', 'exemp@gmail.com', 'masculino');



select * from cliente;


select * from usuario;

select * from produtos;

create table produtos (

id_produto int auto_increment primary key,
nome varchar(30),
descricao varchar(50),
preco varchar(30)

);


insert into produtos values(null, 'telado', 'mouse', '100,00'),

(null, 'caixa de som','som','50,00'),

(null, 'fone de ouvido', 'ouvido', '20,00')



