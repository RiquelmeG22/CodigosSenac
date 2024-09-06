create database Netflix;
create table filme (id_filme int primary key auto_increment, filme_titulo varchar(100) not null, filme_ano_de_producao smallint not null, filme_duracao_em_minutos smallint not null,
 filme_sinopse varchar(500) not null);
use Netflix;
create table serie (id_serie int primary key auto_increment, serie_titulo varchar(100) not null, serie_ano_de_producao smallint not null, serie_sinopse varchar(500) not null);
create table documentario (id_documentario int primary key auto_increment, documentario_ano_de_producao smallint not null, documentario_titulo varchar (100) not null,
documentario_duracao_em_minutos smallint not null, documentario_sinopse varchar(500) not null, documentario_produtora varchar(100));
create table cliente (id_cliente int primary key auto_increment, cliente_numero_cartao_de_credito varchar(30) not null, cliente_endereco varchar(100), cliente_cpf varchar(25) unique not null, 
cliente_nome varchar(50) not null, cliente_senha varchar(70) not null, cliente_email varchar(50) unique not null, cliente_conta_bloqueada bool, cliente_mensalidade_atrasada bool);

create table episodio (id_episodio int primary key auto_increment, episodio_duracao_em_minutos smallint not null, episodio_numero_de_episodio varchar(100) not null, episodio_temporada varchar(100) not null,
episodio_titulo varchar(100) not null, episodio_ano_de_producao smallint not null, episodio_sinopse varchar(500) not null);

create table tipo_videos (id_tipo int primary key auto_increment, tipo_videos_valor varchar(50));

create table assistidos (id_assistidos int primary key auto_increment, assistidos_avaliacao tinyint not null, assistidos_id_tipo int not null, assistidos_id_cliente int not null);

create table ator (id_ator int primary key auto_increment, ator_nome varchar(50) not null, ator_data_de_nascimento date not null, ator_pais varchar(50) not null);

create table particiapacao (id_paraticipaco int primary key auto_increment, participacao_tipo_de_conteudo varchar(50) not null, participacao_id_ator int not null, participacao_id_conteudo int null);

alter table assistidos add foreign key (assistidos_id_cliente) references cliente (id_cliente);



alter table assistidos add foreign key (assistidos_id_tipo) references tipo_videos (id_tipo);

alter table particiapacao add foreign key (participacao_id_ator) references ator (id_ator);











 