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

create table sexo (
idsexo int primary key auto_increment,
tipo varchar(30)
);

create table notafiscal (
    idnotafiscal INT AUTO_INCREMENT PRIMARY KEY,
    sequencia INT NOT NULL,
    emissao DATE NOT NULL,
    vencimento DATE NOT NULL,
    previsao_faturamento DATE,
    aprovacao_cliente BOOLEAN,
    hora_aprovacao TIME,
    embarques INT,
    prazo_entrega INT, -- Prazo de entrega em dias
    n_pedido_compras VARCHAR(50),
    vendedor VARCHAR(100),
    historico TEXT,
    faturamento DECIMAL(10, 2),
    docto VARCHAR(50)
);


INSERT INTO cadcli (nome, telefone_comercial, telefone_resid, cpf, quem_indicou)
VALUES ('João da Silva', '(11) 1234-5678', '(11) 9876-5432', '12345678901', 'Maria Oliveira');


INSERT INTO cadcligeral (
    id_cadcli, aliquota, tabela_preco, transportadora1, transportadora2, 
    regime_de_tributacao, nome, situacao_do_icms, insc_estadual, email, 
    email_danfe, email_de_cobranca, email_loja_virual, telefone_comercial, 
    ramal, tel_celular, fax, cpf, insc_suframa, data_nascm, mod_frete, 
    st_de_cadastro, rg, linha_do_perfil, rua, cep, bairro, cidade, 
    numero, dataNasc, titulo_eleitoral, nivel_de_acesso, rede_social, telefone, 
    idsexo, tipo_contato, valor, descricao, transportadora1, transportadora2, 
    tipo_transacao, comissao, raca, categoria, datacontracao, salario, 
    data_contracao, data_transicao, limite_credito, cnpj, comida_favorita, 
    foto_perfil, gosto_musical, cor_favorita)
VALUES (
    1, 18.00, 100.00, 'Transportadora XYZ', 'Transportadora ABC', 
    'pj', 'João da Silva', 1, '12345678901234', 'joao.silva@example.com', 
    'danfe@exemplo.com', 'cobranca@exemplo.com', 'loja@exemplo.com', '(11) 1234-5678', 
    '123', '(11) 91234-5678', '(11) 8765-4321', '12345678901', '123456789012345', 
    '1980-01-01', 'CIF', 'Ativo', 'MG123456', 'Perfil completo', 'Rua Exemplo', 
    '01234-567', 'Bairro Exemplo', 'Cidade Exemplo', 123, '1980-01-01', 
    '123456789012', 2, 'facebook.com/joaosilva', '(11) 1234-5678', 1, 
    'Comercial', '1000', 'Descrição do cliente', 'Transportadora XYZ', 'Transportadora ABC', 
    'Venda', 0.05, 'Branca', 'VIP', '2024-01-01', 3000.00, 
    '2024-01-01', '2024-12-31', 10000.00, '12.345.678/0001-99', 
    'Pizza', 'foto.jpg', 'Rock', 'Azul'
);

INSERT INTO sexo (tipo)
VALUES ('Masculino');


INSERT INTO notafiscal (
    sequencia, emissao, vencimento, previsao_faturamento, aprovacao_cliente, 
    hora_aprovacao, embarques, prazo_entrega, n_pedido_compras, vendedor, 
    historico, faturamento, docto)
VALUES (
    1, '2024-09-01', '2024-09-30', '2024-09-15', TRUE, 
    '14:30:00', 1, 15, 'PED123456', 'Carlos Santos', 
    'Nota fiscal referente à compra de materiais', 1500.00, 
    'NF123456789'
);
