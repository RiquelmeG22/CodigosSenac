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
id_cadcli int,
aliquota float,
tabela_preco float,
transportadora1 varchar(40),
transportadora2 varchar(40),
regime_de_tributacao enum ('pj', 'pf'),
nome varchar(70),
situacao_do_icms int,
insc_estadual varchar(14),
email varchar(50),
email_danfe varchar(50),
email_de_cobranca varchar(50) , 
email_loja_virual varchar(50) ,
telefone_comercial varchar(20) ,
ramal varchar(20),
tel_celular varchar(20) unique,
fax varchar(20),
cpf char(11) unique,
insc_suframa varchar(20) unique,
data_nascm date,
mod_frete varchar(20),
st_de_cadastro varchar(50),
rg varchar(15) unique,
linha_do_perfil text,
rua varchar(50),
cep varchar(10),
bairro varchar(40),
cidade varchar(40),
numero int,
dataNasc date,
titulo_eleitoral varchar(12) not null,
nivel_de_acesso int,
rede_social varchar(50),
telefone varchar(20),
idsexo int,
tipo_contato varchar(50),
valor varchar(100),
descricao text,
transportadora1 varchar(70),
transportadora2 varchar(70),
tipo_transacao varchar(50),
comissao decimal,
raca varchar(30),
categoria varchar(50),
datacontracao date,
salario decimal,
data_contracao date,
data_transicao date,
limete_credito decimal,
cnpj varchar(17) unique,
comida_favorita varchar(100),
foto_perfil varchar(100),
gosto_musical varchar(100),
cor_favorita varchar(100)
);


