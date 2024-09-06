create database  mateconstrucao;
use mateconstrucao;

create table fornecedores (
cod_forne varchar(10) primary key,
nome varchar(50) not null,
cidade_sede varchar(50) not null,
grupo_cod_fornecedor varchar(10)
);

create table material (
cod_material varchar(10) primary key,
cod_fornecedor varchar(10) not null,
nome varchar(50) not null,
descricao varchar(60)
);

INSERT INTO fornecedores (cod_forne, nome, cidade_sede, grupo_cod_fornecedor) VALUES
('ABC', 'ABC Materiais Eletricos', 'Vitoria', NULL),
('XYZ', 'XYZ Materiais de Escritorio', 'Rio de Janeiro', 'HiX'),
('Hidra', 'Hidra Materiais Hidraulicos', 'Sao Paulo', 'HiX'),
('HiX', 'HidraX Materiais Elétricos e Hidraulicos', 'Sao Paulo', NULL);

insert into material (cod_material, cod_fornecedor, nome, descricao) values
(123, 'ABC', 'Tomada eletrica 10A Nova', 'Tomada eletrica 10A padrao novo'),
(234, 'ABC', 'Disjuntor 25A', 'Disjuntor eletrico 25A'),
(345, 'XYZ', 'Resma Papel A4', 'Resma papel branco A4'),
(456, 'XYZ', 'Toner Imp HR5522', 'Toner impressora HR5522'),
(678, 'Hidra', 'Cano PVC 1/2', 'Cano PVC 1/2 pol'),
(679, 'Hidra', 'Cano PVC 3/4', 'Cano PVC 3/4 pol'),
(680, 'Hidra', 'Medidor hidr 1/2', 'Medidor hidraulico 1/2 pol'),
(681, 'Hidra', 'Joelho 1/2', 'Conector Joelho 1/2 pol'),
(682, 'Hidra', 'Junta 1/2', 'Cano PVC 1/2 pol'),
(1234, 'ABC', 'Tomada eletrica 20A Nova', 'Tomada eletrica 20A padrao novo'),
(2345, 'XYZ', 'Caneta Azul', 'Caneta esferografica azul'),
(4567, 'XYZ', 'Grapeador', 'Grampeador mesa pequeno'),
(4568, 'XYZ', 'Caneta Marca Texto Amarela', 'Caneta Marca Texto Amarela'),
(4569, 'XYZ', 'Lapis HB', 'Lapis Preto HB');


SELECT 
    m.cod_material,
    m.nome AS nome_material,
    m.descricao,
    f.nome AS nome_fornecedor,
    f.cidade_sede
FROM 
    material as m
JOIN 
    fornecedores as f 
ON 
    m.cod_fornecedor = f.cod_forne;
    
SELECT count(*) AS total_materiais FROM material WHERE cod_fornecedor = 'ABC';

SELECT COUNT(*) AS total_materiais FROM material WHERE cod_fornecedor = 'XYZ';

SELECT COUNT(*) AS total_materiais FROM material WHERE cod_fornecedor = 'HIDRA';

SELECT 
    m.cod_material,
    m.nome AS nome_material,
    m.descricao
FROM 
    material AS m
JOIN 
    fornecedores AS f 
ON 
    m.cod_fornecedor = f.cod_forne
WHERE 
    f.cod_forne = 'ABC';
    
SELECT 
    m.cod_material,
    m.nome AS nome_material,
    m.descricao
FROM 
    material AS m
JOIN 
    fornecedores AS f 
ON 
    m.cod_fornecedor = f.cod_forne
WHERE 
    f.cod_forne = 'XYZ';
    
    
SELECT 
    m.cod_material,
    m.nome AS nome_material,
    m.descricao
FROM 
    material AS m
JOIN 
    fornecedores AS f 
ON 
    m.cod_fornecedor = f.cod_forne
WHERE 
    f.cod_forne = 'HIDRA';
    
    

    
    










