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
tabela_preco enum ('', ''),
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
insc_suframa varchar(20) unique,
data_nascm date,
mod_frete enum('', '', ''),
st_de_cadastro enum ('', ''),
rg varchar(15) unique,
linha_do_perfil text ('', '')
);

create table sexo (
IdSexo int primary key auto_increment,
masculino char(1),
feminino char(2),
nao_se_aplica (3)
);


create table transportadora (
IdTransp int primary key auto_increment,
nome varchar(50)
);

create table endereco (
IdEndereco int primary key auto_increment,


);