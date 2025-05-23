
create database ocorrencia;
use ocorrencia;
create table ms (
    qtde int auto_increment not null,
    municipio varchar(50) not null,
    uf char(2) not null,
    regiao varchar(15) not null,
    mes_ano varchar(10) not null,
    vitima int not null,
    primary key (qtde)
);

insert into ms (municipio,uf,regiao,mes_ano,vitima) values
("Água Clara","MS","CENTRO-OESTE","jan/21",0),
("Alcinópolis","MS","CENTRO-OESTE","jan/21",0),
("Amambai","MS","CENTRO-OESTE","jan/21",0),
("Anastácio","MS","CENTRO-OESTE","jan/21",0),
("Anaurilândia","MS","CENTRO-OESTE","jan/21",0),
("Angélica","MS","CENTRO-OESTE","jan/21",0),
("Antônio João","MS","CENTRO-OESTE","jan/21",0),
("Aparecida Do Taboado","MS","CENTRO-OESTE","jan/21",0),
("Aquidauana","MS","CENTRO-OESTE","jan/21",0),
("Aral Moreira","MS","CENTRO-OESTE","jan/21",0),
("Bandeirantes","MS","CENTRO-OESTE","jan/21",0),
("Bataguassu","MS","CENTRO-OESTE","jan/21",0),
("Batayporã","MS","CENTRO-OESTE","jan/21",0),
("Bela Vista","MS","CENTRO-OESTE","jan/21",0),
("Bodoquena","MS","CENTRO-OESTE","jan/21",0),
("Bonito","MS","CENTRO-OESTE","jan/21",0),
("Brasilândia","MS","CENTRO-OESTE","jan/21",0),
("Caarapó","MS","CENTRO-OESTE","jan/21",0),
("Camapuã","MS","CENTRO-OESTE","jan/21",0),
("Campo Grande","MS","CENTRO-OESTE","jan/21",9),
("Caracol","MS","CENTRO-OESTE","jan/21",0),
("Cassilândia","MS","CENTRO-OESTE","jan/21",0),
("Chapadão Do Sul","MS","CENTRO-OESTE","jan/21",0),
("Corguinho","MS","CENTRO-OESTE","jan/21",0),
("Coronel Sapucaia","MS","CENTRO-OESTE","jan/21",1),
("Corumbá","MS","CENTRO-OESTE","jan/21",4),
("Costa Rica","MS","CENTRO-OESTE","jan/21",0),
("Coxim","MS","CENTRO-OESTE","jan/21",1),
("Deodápolis","MS","CENTRO-OESTE","jan/21",0),
("Dois Irmãos Do Buriti","MS","CENTRO-OESTE","jan/21",0),
("Douradina","MS","CENTRO-OESTE","jan/21",0),
("Dourados","MS","CENTRO-OESTE","jan/21",3),
("Eldorado","MS","CENTRO-OESTE","jan/21",0),
("Fátima Do Sul","MS","CENTRO-OESTE","jan/21",1),
("Figueirão","MS","CENTRO-OESTE","jan/21",0),
("Glória De Dourados","MS","CENTRO-OESTE","jan/21",0),
("Guia Lopes Da Laguna","MS","CENTRO-OESTE","jan/21",0),
("Iguatemi","MS","CENTRO-OESTE","jan/21",0),
("Inocência","MS","CENTRO-OESTE","jan/21",0),
("Itaporã","MS","CENTRO-OESTE","jan/21",0),
("Itaquiraí","MS","CENTRO-OESTE","jan/21",1),
("Ivinhema","MS","CENTRO-OESTE","jan/21",1),
("Japorã","MS","CENTRO-OESTE","jan/21",0),
("Jaraguari","MS","CENTRO-OESTE","jan/21",0),
("Jardim","MS","CENTRO-OESTE","jan/21",0),
("Jateí","MS","CENTRO-OESTE","jan/21",0),
("Juti","MS","CENTRO-OESTE","jan/21",0),
("Ladário","MS","CENTRO-OESTE","jan/21",0),
("Laguna Carapã","MS","CENTRO-OESTE","jan/21",0),
("Maracaju","MS","CENTRO-OESTE","jan/21",1),
("Miranda","MS","CENTRO-OESTE","jan/21",2),
("Mundo Novo","MS","CENTRO-OESTE","jan/21",0),
("Naviraí","MS","CENTRO-OESTE","jan/21",0),
("Nioaque","MS","CENTRO-OESTE","jan/21",0),
("Nova Alvorada Do Sul","MS","CENTRO-OESTE","jan/21",0),
("Nova Andradina","MS","CENTRO-OESTE","jan/21",0),
("Novo Horizonte Do Sul","MS","CENTRO-OESTE","jan/21",0),
("Paraíso Das Águas","MS","CENTRO-OESTE","jan/21",0),
("Paranaíba","MS","CENTRO-OESTE","jan/21",0),
("Paranhos","MS","CENTRO-OESTE","jan/21",1),
("Pedro Gomes","MS","CENTRO-OESTE","jan/21",0),
("Ponta Porã","MS","CENTRO-OESTE","jan/21",5),
("Porto Murtinho","MS","CENTRO-OESTE","jan/21",0),
("Ribas Do Rio Pardo","MS","CENTRO-OESTE","jan/21",0),
("Rio Brilhante","MS","CENTRO-OESTE","jan/21",0),
("Rio Negro","MS","CENTRO-OESTE","jan/21",0),
("Rio Verde De Mato Grosso","MS","CENTRO-OESTE","jan/21",0),
("Rochedo","MS","CENTRO-OESTE","jan/21",0),
("Santa Rita Do Pardo","MS","CENTRO-OESTE","jan/21",0),
("São Gabriel Do Oeste","MS","CENTRO-OESTE","jan/21",1),
("Sete Quedas","MS","CENTRO-OESTE","jan/21",0),
("Selvíria","MS","CENTRO-OESTE","jan/21",0),
("Sidrolândia","MS","CENTRO-OESTE","jan/21",0),
("Sonora","MS","CENTRO-OESTE","jan/21",0),
("Tacuru","MS","CENTRO-OESTE","jan/21",0),
("Taquarussu","MS","CENTRO-OESTE","jan/21",0),
("Terenos","MS","CENTRO-OESTE","jan/21",0),
("Três Lagoas","MS","CENTRO-OESTE","jan/21",0),
("Vicentina","MS","CENTRO-OESTE","jan/21",0);




select qtde, municipio, uf, regiao, mes_ano, vitima from ms where municipio = 'Campo Grande';

select qtde, municipio, uf, regiao, mes_ano, vitima from ms where vitima >3 ;

select qtde, municipio, uf, regiao, mes_ano, vitima from ms where vitima = (select max(vitima) from ms);

select qtde, municipio, uf, regiao, mes_ano, vitima from ms where vitima = (select min(vitima) from ms);

select count(*) from ms;

select avg (vitima) from ms;

select * from ms where municipio like 'c%';










