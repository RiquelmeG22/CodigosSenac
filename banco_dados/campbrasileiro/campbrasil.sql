create database campbrasileiro;
use campbrasileiro;


create table gols (
partida_id varchar(100),
rodata varchar(100),
clube varchar(100),
atleta varchar(100), 
minuto varchar(100), 
tipo_de_gol varchar(100)
);

select count(*) from gols;
