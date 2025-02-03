

create database ecommerce; -- faltou a letra a no data base

use ecommerce; -- tem um r no final, a palavra correta é use

---------------------------------------------

create table  produtos ( -- falto um (
    id_prod int(5) primary key auto_increment not null, -- tinha um o no auto_increment , inclui um primary key, 
    nome_prod varchar(100) not null,
    descricao text, -- faltou uma virgula nessa linha
    modelo varchar(50),
    id_categoria int(5), -- faltou uma virgula nessa linha
    id_fabricante int(5) -- tinha uma virgula a mais nessa linha 
    );
    
  

   
create table clientes ( -- faltou o table  
    id_cli int(5) auto_increment not null, -- faltou um _, tinha um char no id
    nome varchar(100) not null,
    cpf int(11),
    telefone varchar(50),
    sexo enum('F','M'), -- faltou uma virgula 
    cadastro datetime, -- a palavra datetime esta escrito errado
    constraint primary key  (id_cli)); -- a palavra primary key esta escrito errado

create table pedidos(
	num_pedido int(5) auto_increment not null,
	data datetime,
	status varchar(50),
	id_cli int(5),
	constraint primary key (num_pedido),
	constraint foreign key (id_cli) references clientes(id_cli)
    );

   
create table pedido_item( 
	idtem_pedido int(5) auto_increment not null,
	num_pedido int(5) not null,
	qtde int(5) not null,
	valor_unit decimal(10,2),
	total decimal(10,2),
	id_prod int(5),
	constraint primary key (idtem_pedido),
	constraint foreign key (num_pedido) references pedidos(num_pedido), -- o primary key estava escrito errado
	constraint foreign key (id_prod) references produtos(id_prod) -- o primary key estava escrito errado
);
  
    

create table estoque_produtos(
	id_estoque int(5) auto_increment, -- faltou auto_increment
	quantidade int(5) not null,
	quant_min int(5),
	id_prod int(5), -- faltou o 
	constraint primary key (id_estoque),
	constraint foreign key (id_prod) references produtos(id_prod)
);



insert into clientes values (null,'João','02102202324','6799999999','M',now()); -- faltou um r , e tinha 2 comando na mesma linha
insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());
   
insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);
   
insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
insert into produtos values (null, 'Processador AMD','4.2Ghz','Ryzen5',null,null); -- faltou ' e , 



insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null); -- faltou , e '

   
select * from produtos; -- from estava escrito errado
describe estoque_produtos; -- describe estava escrito errado


insert into estoque_produtos values (null,80,10,1);
insert into estoque_produtos values (null,44,5,9); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,55,5,8); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,36,5,7); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,49,5,6); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,100,5,1); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,100,5,2); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,100,5,3); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,100,5,4); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado
insert into estoque_produtos values (null,100,5,5); -- into tava escrito errado, values estava escrito errado, produtos estava escrito errado


 