create database estrutura;
use estrutura;

create table cliente (
id_codcliente int primary key auto_increment,
cliente_nome varchar(50) not null,
cliente_data_nascimento varchar(15) not null,
cliente_cpf char(11) unique not null

);

create table pedido (
id_codpedido int primary key auto_increment,
id_codcliente int unsigned not null,
pedido_data_de_pedido varchar(10) not null,
pedido_nf varchar(10) not null,
pedido_valor_total float not null
);

create table produto (
id_codproduto int primary key auto_increment,
produto_descricao text not null,
produto_quantidade int unsigned not null
);

create table item_pedido (
	id_codpedido int auto_increment,
	item_pedido_numero_item int not null,
	item_pedido_valor_unitario int not null,
	item_pedido_quantidade int not null,
	id_codproduto int unsigned not null,
	primary key (id_codpedido, item_pedido_numero_item),
    foreign key (id_codpedido) references pedido (id_codpedido),
    foreign key (item_pedido_numero_item) references pedido (id_codpedido)
);

create table log (
id_codlog int primary key auto_increment,
log_data varchar(10) not null,
log_descricao text not null
);

create table req_compra (
id_req_compra int primary key auto_increment,
id_codproduto int not null, 
rq_compra_data varchar(10) not null,
rq_compra_quantidade int not null,
foreign key (id_req_compra) references produto(id_codproduto)
);


INSERT INTO cliente (cliente_nome, cliente_data_nascimento, cliente_cpf) VALUES
('Ana Silva', '1985-04-15', '12345678901'),
('Carlos Pereira', '1990-06-22', '23456789012'),
('Maria Oliveira', '1978-12-01', '34567890123'),
('João Santos', '1983-08-30', '45678901234'),
('Fernanda Costa', '1992-03-17', '56789012345'),
('Roberto Lima', '1980-11-09', '67890123456'),
('Patrícia Gomes', '1987-01-25', '78901234567'),
('Ricardo Martins', '1995-07-10', '89012345678'),
('Juliana Souza', '1989-05-14', '90123456789'),
('Eduardo Almeida', '1982-09-03', '01234567890');




INSERT INTO produto (produto_descricao, produto_quantidade) VALUES
('Cadeira de Escritório', 50),
('Mesa de Reunião', 30),
('Computador Desktop', 15),
('Impressora a Laser', 10),
('Teclado Mecânico', 100),
('Mouse Óptico', 75),
('Monitor LED 24"', 20),
('Fone de Ouvido', 40),
('Projetor Full HD', 8),
('Cadeira Gamer', 25);

INSERT INTO pedido (id_codcliente, pedido_data_de_pedido, pedido_nf, pedido_valor_total) VALUES
(1, '2024-06-15', '2024061501', 320.75),
(2, '2024-06-20', '2024061502', 150.00),
(3, '2024-07-05', '2024070501', 250.40),
(4, '2024-07-10', '2024071001', 680.00),
(5, '2024-07-20', '2024072001', 405.25);


INSERT INTO item_pedido (id_codpedido, item_pedido_numero_item, item_pedido_valor_unitario, item_pedido_quantidade, id_codproduto) VALUES
(1, 1, 150.00, 2, 1),   -- Pedido 1, Item 1, Produto com ID 1
(1, 2, 75.00, 1, 2),    -- Pedido 1, Item 2, Produto com ID 2
(2, 1, 300.00, 1, 3),   -- Pedido 2, Item 1, Produto com ID 3
(3, 1, 120.00, 3, 4),   -- Pedido 3, Item 1, Produto com ID 4
(3, 2, 80.00, 2, 5);    -- Pedido 3, Item 2, Produto com ID 5

select * from item_pedido;










