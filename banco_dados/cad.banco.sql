create database cadbanco;
use cadbanco;

create table cadcli (
id_cadcli int primary key auto_increment,
nome varchar(70),
telefone_comercial varchar(20) unique,
telefone_resid varchar(20) unique,
cpf char(11) unique,
quem_indicou varchar(70)
);

create table cadcligeral (
id_cadcligeral int primary key auto_increment,
aliquota float,
tabela_preco float,
transportadora1 varchar(40),
transportadora2 varchar(40),
regime_de_tributacao enum ('pj', 'pf'),
nome varchar(70),
situacao_do_icms int,
insc_estadual varchar(14),
email varchar(50) unique,
email_danfe varchar(50) unique,
email_de_cobranca varchar(50) unique, 
email_loja_virual varchar(50) unique,
telefone_comercial varchar(20) unique,
ramal varchar(20),
tel_celular varchar(20) unique,
fax varchar(20),
cpf char(11) unique,
data_nascm date
);