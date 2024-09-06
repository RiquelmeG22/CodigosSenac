create database cadastro;
 create table estado (
 id_estado int auto_increment primary key, 
 nome varchar(100)
 );
 
 create table cidade (
 id_cidade int auto_increment primary key, 
 nome varchar(100)
 );
 
 
  create table pessoa (
 id int auto_increment primary key, 
 nome varchar(100),
 id_estado int,
 id_cidade int, 
 foreign key fk_cidade (id_cidade) references cidade (id_cidade),
  foreign key fk_estado (id_estado) references estado (id_estado)
 );
 
 
 insert into cidade values
 (null, "Campo Grande"),
 (null, "Dourados"),
 (null, "Tres Lagoas"),
 (null, "Corumbá"),
 (null, "Cuiabá"),
 (null, "Goiania");

 
 insert into estado values 
 (null, "Mato Grosso"), 
 (null, "Mato Grosso Do Sul"),
 (null, "Goias"),
 (null, "Parana"),
 (null, "Sao Paulo"),
 (null, "Rio Grande Do Sul");
 
 insert into pessoa values
 (null, "Ederson da Costa", 1,2),
 (null, "Maria Aperecida", 2,2),
 (null, "Pedro Correira", 1,3),
 (null, "Michael Jackson", 2,3),
 (null, "Fredie Mercury", 3,5);
 
 
 select * from pessoa;
 
 select pessoa.nome, cidade.nome, estado.nome from pessoa join cidade on pessoa.id_cidade = cidade.id_cidade join estado on pessoa.id_estado = estado.id_estado;
 select pessoa.nome, cidade.nome, estado.nome from pessoa left join cidade on pessoa.id_cidade = cidade.id_cidade left join estado on pessoa.id_estado = estado.id_estado; 
 select pessoa.nome, cidade.nome, estado.nome from pessoa right join cidade on pessoa.id_cidade = cidade.id_cidade right join estado on pessoa.id_estado = estado.id_estado; 
 select pessoa.nome, cidade.nome, estado.nome from pessoa cross join cidade cross join estado;
 
 select pessoa.nome from pessoa union select estado.nome from estado; 
 
 
 
 
 
 
 