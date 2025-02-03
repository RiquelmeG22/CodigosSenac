create database cadcliente2;
use cadcliente2;


create table escolaridade (
id_escolaridade int primary key auto_increment,
escolaridade varchar(50) 
);

create table raca (
id_raca int primary key auto_increment,
raca varchar(20) not null
);

create table nacionalidade (
id_nacionalidade int primary key auto_increment,
nacionalidade varchar(40) 
);

create table sexo (
id_sexo int primary key auto_increment,
sexo char(3) not null
);

create table estado (
id_estado int primary key auto_increment,
estado varchar(50) not null
);

create table cidade (
id_cidade int primary key auto_increment,
cidade varchar(50) not null,
id_estado int,
foreign key fk_estado(id_estado) references estado(id_estado)
);


create table estado_civil ( 
id_estado_civil int primary key auto_increment, 
estado_civil varchar(20) not null
);

create table clientes (
cpf char(15) primary key,
clientes_nome varchar(70),
clientes_rg char(11) unique,
id_cidade int,
id_sexo int,
id_nacionalidade int,
clientes_fone varchar(20) not null,
id_raca int,
id_escolaridade int,
id_estado_civil int, 
foreign key fk_estado_civil(id_estado_civil) references estado_civil(id_estado_civil),
foreign key fk_cidade(id_cidade) references cidade(id_cidade),
foreign key fk_sexo(id_sexo) references sexo(id_sexo),
foreign key fk_nacionalidade(id_nacionalidade) references nacionalidade(id_nacionalidade),
foreign key fk_raca(id_raca) references raca(id_raca),
foreign key fk_escolaridade(id_escolaridade) references escolaridade(id_escolaridade)
);


insert into estado_civil(estado_civil) values 
('Solteiro'),
('Casado'),
('Divorciado'),
('Viúvo'),
('Separado');




insert into estado(estado) values

('Acre'),
('Alagoas'),
('Amapá'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');


INSERT INTO cidade (cidade, id_estado) VALUES
('Rio Branco', 1),
('Cruzeiro do Sul', 1),
('Senador Guiomard', 1),
('Tarauacá', 1),
('Feijó', 1),
('Maceió', 2),
('Arapiraca', 2),
('Palmeira dos Índios', 2),
('São Miguel dos Campos', 2),
('Delmiro Gouveia', 2),
('Macapá', 3),
('Santana', 3),
('Laranjal do Jari', 3),
('Oiapoque', 3),
('Mazagão', 3),
('Manaus', 4),
('Parintins', 4),
('Itacoatiara', 4),
('Coari', 4),
('Manacapuru', 4),
('Salvador', 5),
('Feira de Santana', 5),
('Vitória da Conquista', 5),
('Camaçari', 5),
('Ilhéus', 5),
('Fortaleza', 6),
('Caucaia', 6),
('Juazeiro do Norte', 6),
('Sobral', 6),
('Crato', 6),
('Brasília', 7),
('Taguatinga', 7),
('Ceilândia', 7),
('Planaltina', 7),
('Gama', 7),
('Vitória', 8),
('Vila Velha', 8),
('Cariacica', 8),
('Serra', 8),
('Guarapari', 8),
('Goiânia', 9),
('Anápolis', 9),
('Aparecida de Goiânia', 9),
('Luziânia', 9),
('Cidade Ocidental', 9),
('São Luís', 10),
('Imperatriz', 10),
('Timon', 10),
('Caxias', 10),
('Balsas', 10),
('Cuiabá', 11),
('Várzea Grande', 11),
('Rondonópolis', 11),
('Sinop', 11),
('Tangará da Serra', 11),
('Campo Grande', 12),
('Dourados', 12),
('Três Lagoas', 12),
('Corumbá', 12),
('Ponta Porã', 12),
('Belo Horizonte', 13),
('Uberlândia', 13),
('Contagem', 13),
('Juiz de Fora', 13),
('Montes Claros', 13),
('Belém', 14),
('Ananindeua', 14),
('Santarém', 14),
('Marabá', 14),
('Paragominas', 14),
('João Pessoa', 15),
('Campina Grande', 15),
('Santa Rita', 15),
('Patos', 15),
('Bayeux', 15),
('Curitiba', 16),
('Londrina', 16),
('Maringá', 16),
('Ponta Grossa', 16),
('Foz do Iguaçu', 16),
('Recife', 17),
('Olinda', 17),
('Jaboatão dos Guararapes', 17),
('Caruaru', 17),
('Petrolina', 17),
('Teresina', 18),
('Parnaíba', 18),
('Picos', 18),
('Floriano', 18),
('Oeiras', 18),
('Rio de Janeiro', 19),
('Niterói', 19),
('São Gonçalo', 19),
('Duque de Caxias', 19),
('Nova Iguaçu', 19),
('Natal', 20),
('Mossoró', 20),
('Parnamirim', 20),
('Caicó', 20),
('São Gonçalo do Amarante', 20),
('Porto Alegre', 21),
('Caxias do Sul', 21),
('Pelotas', 21),
('Santa Maria', 21),
('Novo Hamburgo', 21),
('Porto Velho', 22),
('Ji-Paraná', 22),
('Ariquemes', 22),
('Vilhena', 22),
('Rolim de Moura', 22),
('Boa Vista', 23),
('Rorainópolis', 23),
('Caracaraí', 23),
('Mucajaí', 23),
('Cantá', 23),
('Florianópolis', 24),
('Joinville', 24),
('Blumenau', 24),
('Chapecó', 24),
('Criciúma', 24),
('São Paulo', 25),
('Campinas', 25),
('Santos', 25),
('São Bernardo do Campo', 25),
('São José dos Campos', 25),
('Aracaju', 26),
('Nossa Senhora do Socorro', 26),
('Itabaiana', 26),
('Lagarto', 26),
('Estância', 26),
('Palmas', 27),
('Araguaína', 27),
('Gurupi', 27),
('Paraíso do Tocantins', 27),
('Porto Nacional', 27);



insert into sexo(sexo) values
('M'),
('F'),
('O');

insert into nacionalidade(nacionalidade) values
("Brasileira"),
("Estrangeira");

insert into raca(raca) values
('Branco'),
('Pardo '),
('Amarelo '),
('Negro '),
('Indígena');


insert into escolaridade(escolaridade) values
('Educação Infantil'),
('Ensino Fundamental'),
('Ensino Médio'),
('Educação Profissional (ou Técnico)'),
('Ensino Superior'),
('Educação de Jovens e Adultos (EJA)'),
('Educação a Distância (EaD)'),
('Educação Continuada ou Formação ao Longo da Vida');

insert into clientes (cpf, clientes_nome, clientes_rg, id_cidade, id_sexo, id_nacionalidade, clientes_fone, id_raca, id_escolaridade, id_estado_civil) values
('111.222.333-44', 'Aline Pereira', '087654321', 1, 1, 1, '(11) 91234-5678', 1, 3, 1),
('122.233.344-55', 'Bruno Martins', '276543210', 2, 2, 1, '(21) 92345-6789', 2, 4, 2),
('133.244.455-66', 'Carla Costa', '465432109', 3, 1, 2, '(31) 93456-7890', 3, 5, 3),
('144.355.566-77', 'Daniela Silva', '154321098', 4, 2, 2, '(41) 94567-8901', 1, 2, 4),
('155.466.677-88', 'Eduardo Almeida', '243210987', 5, 1, 2, '(51) 95678-9012', 2, 1, 2),
('166.577.788-99', 'Fernanda Rocha', '032109876', 6, 2, 1, '(61) 96789-0123', 3, 4, 1),
('177.688.899-00', 'Gabriel Oliveira', '521098765', 7, 1, 1, '(71) 97890-1234', 1, 1, 3),
('188.799.900-11', 'Helena Lima', '610987654', 8, 2, 1, '(81) 98901-2345', 2, 3, 1),
('199.800.011-22', 'Igor Santos', '609876543', 9, 1, 2, '(91) 99012-3456', 3, 2, 3),
('200.911.122-33', 'Juliana Ferreira', '128765432', 10, 2, 2, '(11) 99123-4567', 1, 1, 4),
('211.022.233-44', 'Kleber Martins', '347654321', 11, 1, 2, '(21) 99234-5678', 2, 4, 1),
('222.133.344-55', 'Larissa Costa', '566543210', 12, 2, 1, '(31) 99345-6789', 3, 5, 1),
('233.244.455-66', 'Marcelo Souza', '335432109', 13, 1, 1, '(41) 99456-7890', 1, 2, 1),
('244.355.566-77', 'Natália Lima', '774321098', 14, 2, 1, '(51) 99567-8901', 2, 3, 4),
('255.466.677-88', 'Otávio Pereira', '883210987', 15, 1, 2, '(61) 99678-9012', 3, 4, 2),
('266.577.788-99', 'Priscila Rocha', '992109876', 16, 2, 2, '(71) 99789-0123', 1, 5, 2),
('277.688.899-00', 'Quintino Santos', '221098765', 17, 1, 2, '(81) 99890-1234', 2, 1, 1),
('288.799.900-11', 'Raquel Almeida', '220987654', 18, 2, 1, '(91) 99901-2345', 3, 2, 2),
('299.800.011-22', 'Sérgio Oliveira', '189876543', 19, 1, 1, '(11) 90012-3456', 1, 3, 3),
('300.911.122-33', 'Tatiane Costa', '198765432', 20, 2, 1, '(21) 91123-4567', 2, 4, 4);




SELECT  c.clientes_nome AS Nome, ci.cidade AS Cidade FROM clientes c JOIN cidade ci ON c.id_cidade = ci.id_cidade;

SELECT c.clientes_nome AS Nome, e.estado AS Estado FROM clientes c JOIN cidade ci ON c.id_cidade = ci.id_cidade JOIN estado e ON ci.id_estado = e.id_estado;

SELECT c.clientes_nome AS Nome, c.cpf AS CPF, r.raca AS Raca FROM clientes c JOIN raca r ON c.id_raca = r.id_raca;

SELECT c.clientes_nome AS Nome, n.nacionalidade AS Nacionalidade FROM clientes c JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade;

SELECT c.clientes_nome AS Nome, e.escolaridade AS Escolaridade FROM clientes c JOIN escolaridade e ON c.id_escolaridade = e.id_escolaridade;

SELECT c.clientes_nome AS Nome, ci.cidade AS Cidade, e.estado AS Estado FROM  clientes c JOIN cidade ci ON c.id_cidade = ci.id_cidade JOIN estado e ON ci.id_estado = e.id_estado;

SELECT 
    c.clientes_nome AS Nome, 
    ci.cidade AS Cidade, 
    e.estado AS Estado,
    c.clientes_fone AS Fone,
    c.clientes_rg AS RG,
    s.sexo AS Sexo,
    n.nacionalidade AS Nacionalidade,
    r.raca AS Raca,
    es.escolaridade AS Escolaridade
FROM 
    clientes c
JOIN 
    cidade ci ON c.id_cidade = ci.id_cidade
JOIN 
    estado e ON ci.id_estado = e.id_estado
JOIN 
    sexo s ON c.id_sexo = s.id_sexo
JOIN 
    nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade
JOIN 
    raca r ON c.id_raca = r.id_raca
JOIN 
    escolaridade es ON c.id_escolaridade = es.id_escolaridade;


update cidade set cidade ='Abaixo de M' where cidade between "A%" and "M%"; 
SET SQL_SAFE_UPDATES = 0;
select * from cidade;

update cidade set cidade ='Acima de M' where cidade between "N%" and "Z%";
select * from cidade;

select * from cidade where cidade between "N%" and "Z%";

select * from estado where estado regexp '^(Amazonas|Pará|Acre|Roraima|Rondônia|Amapá|Tocantins)';

select * from estado where estado regexp '^(Alagoas|Bahia|Ceará|Maranhão|Paraíba|Pernambuco|Piauí|Rio Grande do Norte|Sergipe)';

select * from estado where estado regexp '^(Goiás|Mato Grosso|Mato Grosso Do Sul|Distrito Federal)';

select * from estado where estado regexp '^(São Paulo|Rio de Janeiro|Espírito Santo|Minas Gerais)';

select * from estado where estado regexp '^(Paraná|Santa Catarina|Rio Grande do Sul)';

UPDATE estado set estado = "Centro-Oeste" where estado regexp '^(Goiás|Mato Grosso|Centro-Oeste|Distrito Federal)';
select * from estado;

UPDATE nacionalidade set nacionalidade = "Fora do Brasil" where nacionalidade = 'Estrangeira';
select * from nacionalidade;

UPDATE raca set raca = "Ser Humano";
select * from raca;

update escolaridade set escolaridade = "Ensino Básico" where id_escolaridade <4;
select * from escolaridade;


update escolaridade set escolaridade = "Ensino Avançado" where id_escolaridade >=4;
select * from escolaridade;






































