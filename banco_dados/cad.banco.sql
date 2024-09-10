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
insc_suframa varchar(20) unique,
data_nascm date,
mod_frete enum('', '', ''),
st_de_cadastro enum ('', ''),
rg varchar(15) unique,
linha_do_perfil text ('', '')
);

create table sexo (
idSexo int primary key auto_increment,
tipo varchar(20)
);


create table transportadora (
idTransp int primary key auto_increment,
nome varchar(50)
);

create table endereco (
idEndereco int primary key auto_increment,
rua varchar(50),
cep varchar(8),
bairro varchar(40),
cidade varchar(40),
numero int
);

create table perfil (
idPerfil int primary key auto_increment,
nome varchar(70),
telefone varchar(20) unique,
email varchar(50) unique,
dataNasc date
);

create table comunicacao (
idcomunicacao int primary key auto_increment,
tipocontato varchar(50),
valor varchar(100), 
descricao text,
rede social varchar(50)
);

create table vendedor (
idvendedor int primary key auto_increment,
nome varchar(70),
datanasc date,
email varchar(50) unique,
salario decimal (10, 2)
);

create table financeiro (
idfananceiro int primary key auto_increment,
tipo_transacao varchar(50),
categoria varchar(50),
descricao text,
data_transicao date,
);