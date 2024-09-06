create database Netflix;
create table filme (id_filme int primary key auto_increment, filme_titulo varchar(100) not null, filme_ano_de_producao smallint not null, filme_duracao_em_minutos smallint not null,
 filme_sinopse varchar(500) not null);
use Netflix;
create table serie (id_serie int primary key auto_increment, serie_titulo varchar(100) not null, serie_ano_de_producao smallint not null,
 serie_sinopse varchar(500) not null, serie_id_temporada int not null);
 
 

create table documentario (id_documentario int primary key auto_increment, documentario_ano_de_producao smallint not null, documentario_titulo varchar (100) not null,
documentario_duracao_em_minutos smallint not null, documentario_sinopse varchar(500) not null, documentario_produtora varchar(100));

create table cliente (id_cliente int primary key auto_increment, cliente_numero_cartao_de_credito varchar(30) not null, cliente_endereco varchar(100), cliente_cpf varchar(25) unique not null, 
cliente_nome varchar(50) not null, cliente_senha varchar(70) not null, cliente_email varchar(50) unique not null, cliente_conta_bloqueada bool, cliente_mensalidade_atrasada bool);

create table episodio (id_episodio int primary key auto_increment, episodio_duracao_em_minutos smallint not null, episodio_numero_de_episodio varchar(100) not null, episodio_temporada varchar(100) not null,
episodio_titulo varchar(100) not null, episodio_ano_de_producao smallint not null, episodio_sinopse varchar(500) not null, episodio_id_temporada int not null);



create table tipo_videos (id_tipo int primary key auto_increment, tipo_videos_valor varchar(50));

create table assistidos (id_assistidos int primary key auto_increment, assistidos_avaliacao tinyint not null, assistidos_id_tipo int not null, assistidos_id_cliente int not null);

create table ator (id_ator int primary key auto_increment, ator_nome varchar(50) not null, ator_data_de_nascimento date not null, ator_pais varchar(50) not null);

create table particiapacao (id_paraticipaco int primary key auto_increment, participacao_tipo_de_conteudo varchar(50) not null, participacao_id_ator int not null, participacao_id_conteudo int null);

create table temporada (id_temporada int primary key auto_increment, temporada_nome_da_temporada varchar(50) not null);

alter table assistidos add foreign key (assistidos_id_cliente) references cliente (id_cliente);

alter table assistidos add foreign key (assistidos_id_tipo) references tipo_videos (id_tipo);

alter table particiapacao add foreign key (participacao_id_ator) references ator (id_ator);

alter table serie add foreign key (serie_id_temporada) references temporada (id_temporada);

alter table episodio add foreign key (episodio_id_temporada) references temporada (id_temporada);


INSERT INTO cliente (
    cliente_numero_cartao_de_credito,
    cliente_endereco,
    cliente_cpf,
    cliente_nome,
    cliente_senha,
    cliente_email,
    cliente_conta_bloqueada,
    cliente_mensalidade_atrasada
) VALUES
    ('1234-5678-9012-3456', 'Rua A, 123, Centro', '123.456.789-00', 'João Silva', 'senha123', 'joao.silva@email.com', 0, 0),
    ('2345-6789-0123-4567', 'Rua B, 456, Jardim', '234.567.890-11', 'Maria Oliveira', 'senha456', 'maria.oliveira@email.com', 0, 1),
    ('3456-7890-1234-5678', 'Rua C, 789, Vila', '345.678.901-22', 'Carlos Santos', 'senha789', 'carlos.santos@email.com', 1, 0),
    ('4567-8901-2345-6789', 'Rua D, 101, Bairro', '456.789.012-33', 'Ana Costa', 'senha101', 'ana.costa@email.com', 0, 0),
    ('5678-9012-3456-7890', 'Rua E, 202, Zona Norte', '567.890.123-44', 'Pedro Almeida', 'senha202', 'pedro.almeida@email.com', 1, 1),
    ('6789-0123-4567-8901', 'Rua F, 303, Zona Sul', '678.901.234-55', 'Laura Martins', 'senha303', 'laura.martins@email.com', 0, 1),
    ('7890-1234-5678-9012', 'Rua G, 404, Centro Oeste', '789.012.345-66', 'Roberto Lima', 'senha404', 'roberto.lima@email.com', 1, 0),
    ('8901-2345-6789-0123', 'Rua H, 505, Centro Leste', '890.123.456-77', 'Juliana Ferreira', 'senha505', 'juliana.ferreira@email.com', 0, 0);
    
    INSERT INTO episodio (
    episodio_duracao_em_minutos,
    episodio_numero_de_episodio,
    episodio_temporada,
    episodio_titulo,
    episodio_ano_de_producao,
    episodio_sinopse
) VALUES
    (45, 'E01', 'Temporada 1', 'O Começo de Tudo', 2023, 'A introdução da série, onde conhecemos os personagens principais e o cenário principal da trama.'),
    (50, 'E02', 'Temporada 1', 'Novos Desafios', 2023, 'Os protagonistas enfrentam novos desafios que testam suas habilidades e amizades.'),
    (52, 'E03', 'Temporada 1', 'A Revelação', 2023, 'Uma grande revelação muda o rumo da história e deixa todos surpresos.'),
    (48, 'E04', 'Temporada 1', 'O Grande Conflito', 2023, 'Os conflitos entre os personagens atingem seu ponto máximo, levando a uma grande confrontação.'),
    (47, 'E05', 'Temporada 2', 'O Retorno', 2024, 'A segunda temporada começa com o retorno de um personagem crucial e novas questões em aberto.'),
    (49, 'E06', 'Temporada 2', 'Segredos do Passado', 2024, 'Segredos do passado dos personagens são revelados, trazendo novas dinâmicas para a trama.'),
    (46, 'E07', 'Temporada 2', 'Reviravolta', 2024, 'Uma reviravolta inesperada altera a trajetória da história e coloca todos em perigo.'),
    (51, 'E08', 'Temporada 2', 'O Grande Desfecho', 2024, 'O desfecho da temporada traz respostas para muitas perguntas e prepara o terreno para a próxima temporada.');
    
    INSERT INTO filme (
    filme_titulo,
    filme_ano_de_producao,
    filme_duracao_em_minutos,
    filme_sinopse
) VALUES
    ('A Jornada do Herói', 2023, 120, 'Um jovem descobriu que possui habilidades especiais e deve embarcar em uma jornada para salvar o mundo de uma ameaça iminente.'),
    ('O Mistério da Cidade Perdida', 2022, 135, 'Um arqueólogo e sua equipe tentam desvendar os segredos de uma antiga cidade perdida e enfrentar perigos desconhecidos.'),
    ('A Última Esperança', 2024, 110, 'Em um futuro distópico, um grupo de rebeldes luta contra um regime opressor para garantir a sobrevivência da humanidade.'),
    ('Entre Mundos', 2021, 140, 'Uma jovem descobre a existência de um portal para um universo paralelo e deve escolher entre dois mundos conflitantes.'),
    ('O Voo da Liberdade', 2023, 115, 'Baseado em uma história real, este filme narra a corajosa fuga de um grupo de prisioneiros durante a Segunda Guerra Mundial.'),
    ('Coração de Ferro', 2024, 125, 'Um engenheiro e um piloto se unem para desenvolver uma nova tecnologia que pode mudar o curso da guerra em um futuro distante.'),
    ('A Noite do Destino', 2022, 100, 'Durante uma tempestade, um grupo de estranhos fica preso em uma casa e descobre segredos obscuros que podem mudar suas vidas para sempre.'),
    ('Sombras do Passado', 2023, 130, 'Um detetive investiga uma série de crimes que parecem estar conectados a um evento traumático do seu próprio passado.');
    
    INSERT INTO serie (
    serie_titulo,
    serie_ano_de_producao,
    serie_sinopse
) VALUES
    ('Exploradores do Tempo', 2023, 'Um grupo de cientistas desenvolve uma máquina do tempo e viaja para diferentes períodos históricos, enfrentando perigos e desafios enquanto tentam corrigir anomalias temporais.'),
    ('A Última Fronteira', 2022, 'Em um futuro próximo, uma equipe de exploradores espaciais embarca em uma missão para explorar os confins do universo e encontrar novos mundos habitáveis.'),
    ('Segredos da Cidade Subterrânea', 2024, 'Após um desabamento em uma grande cidade, uma equipe de resgate descobre uma civilização subterrânea secreta com suas próprias leis e mistérios.'),
    ('O Enigma dos Deuses', 2021, 'Uma jovem arqueóloga descobre artefatos antigos que podem estar ligados a uma antiga raça de deuses e deve desvendar os segredos por trás desses mistérios.'),
    ('Redemoinho de Emoções', 2023, 'A série segue a vida de quatro amigos que enfrentam desafios pessoais e relacionamentos complicados enquanto tentam equilibrar suas vidas profissionais e pessoais.'),
    ('Pacto das Sombras', 2024, 'Em uma pequena cidade, um grupo de adolescentes descobre que possuem habilidades sobrenaturais e precisam enfrentar uma ameaça oculta que ameaça a cidade.'),
    ('Caminhos Cruzados', 2022, 'A trama gira em torno de várias histórias interligadas sobre pessoas cujas vidas se cruzam de maneiras inesperadas, mostrando como cada uma impacta a outra.'),
    ('A Jornada dos Heróis', 2023, 'Um grupo de heróis improváveis se une para enfrentar uma ameaça que coloca em risco a sobrevivência do mundo, passando por diversas aventuras e desafios.');


INSERT INTO documentario (
    documentario_ano_de_producao,
    documentario_titulo,
    documentario_duracao_em_minutos,
    documentario_sinopse,
    documentario_produtora
) VALUES
    (2023, 'Os Segredos da Natureza', 90, 'Um mergulho profundo nos ecossistemas mais inexplorados do planeta, revelando a complexa interação entre as espécies e seu ambiente.', 'Nature Films Inc.'),
    (2022, 'A História das Civilizações', 120, 'Uma análise detalhada das civilizações antigas e suas contribuições para o mundo moderno, explorando artefatos, arquitetura e culturas.', 'History Channel Productions'),
    (2024, 'Cidades do Futuro', 85, 'Explora as inovações tecnológicas e arquitetônicas que estão moldando as cidades do futuro, desde sistemas de transporte até edifícios sustentáveis.', 'Future Vision Studios'),
    (2021, 'O Impacto das Mudanças Climáticas', 100, 'Examina como as mudanças climáticas estão afetando diferentes partes do mundo e as medidas que estão sendo tomadas para combater seus efeitos.', 'Global Earth Media'),
    (2023, 'A Era dos Dinossauros', 95, 'Um olhar fascinante sobre a vida dos dinossauros, com base nas descobertas mais recentes e tecnologias avançadas de visualização.', 'Dinosaurs Revealed Ltd.'),
    (2024, 'Gênios da Tecnologia', 110, 'Destaca as mentes brilhantes por trás das maiores inovações tecnológicas dos últimos anos e como suas invenções estão transformando o mundo.', 'Tech Innovators Co.'),
    (2022, 'Maravilhas Subaquáticas', 80, 'Uma exploração das belezas e mistérios dos oceanos, revelando a vida marinha em sua forma mais deslumbrante e inexplorada.', 'Oceanic Wonders Films'),
    (2023, 'Exploração Espacial: Missões Futuras', 105, 'Analisa as futuras missões espaciais planejadas para explorar nosso sistema solar e além, incluindo os desafios e objetivos das principais agências espaciais.', 'Space Frontier Productions');

    
INSERT INTO tipo_videos (
    tipo_videos_valor
) VALUES
    ('Filme'),       -- Tipo 1: Filme
    ('Série'),       -- Tipo 2: Série
    ('Documentário'),-- Tipo 3: Documentário
    ('Minissérie'),  -- Tipo 4: Minissérie
    ('Especial'),    -- Tipo 5: Especial
    ('Curta-metragem'), -- Tipo 6: Curta-metragem
    ('Programa'),    -- Tipo 7: Programa
    ('Documentário Curto'); -- Tipo 8: Documentário Curto
    
    
INSERT INTO ator (
    ator_nome,
    ator_data_de_nascimento,
    ator_pais
) VALUES
    ('Leonardo DiCaprio', '1974-11-11', 'Estados Unidos'),
    ('Natalie Portman', '1981-06-09', 'Israel'),
    ('Javier Bardem', '1969-03-01', 'Espanha'),
    ('Cate Blanchett', '1969-05-14', 'Austrália'),
    ('Idris Elba', '1972-09-06', 'Reino Unido'),
    ('Penélope Cruz', '1974-04-28', 'Espanha'),
    ('Denzel Washington', '1954-12-28', 'Estados Unidos'),
    ('Tilda Swinton', '1960-11-05', 'Reino Unido');
    
    

    INSERT INTO participacoes (
    participacao_tipo_de_conteudo,
    participacao_id_ator,
    participacao_id_conteudo
) VALUES
    ('Filme', 1, 1),   -- Ator 1 participa no Conteúdo 1 (Filme)
    ('Série', 2, 2),   -- Ator 2 participa no Conteúdo 2 (Série)
    ('Documentário', 3, 3), -- Ator 3 participa no Conteúdo 3 (Documentário)
    ('Filme', 4, 4),   -- Ator 4 participa no Conteúdo 4 (Filme)
    ('Série', 5, 5),   -- Ator 5 participa no Conteúdo 5 (Série)
    ('Documentário', 6, 6), -- Ator 6 participa no Conteúdo 6 (Documentário)
    ('Filme', 7, 7),   -- Ator 7 participa no Conteúdo 7 (Filme)
    ('Série', 8, 8);   -- Ator 8 participa no Conteúdo 8 (Série)
    
    
INSERT INTO particiapacao (
    participacao_tipo_de_conteudo,
    participacao_id_ator,
    participacao_id_conteudo
) VALUES
    ('Filme', 1, 1),   -- Ator 1 participa no Conteúdo 1 (Filme)
    ('Série', 2, 2),   -- Ator 2 participa no Conteúdo 2 (Série)
    ('Documentário', 3, 3), -- Ator 3 participa no Conteúdo 3 (Documentário)
    ('Filme', 4, 4),   -- Ator 4 participa no Conteúdo 4 (Filme)
    ('Série', 5, 5),   -- Ator 5 participa no Conteúdo 5 (Série)
    ('Documentário', 6, 6), -- Ator 6 participa no Conteúdo 6 (Documentário)
    ('Filme', 7, 7),   -- Ator 7 participa no Conteúdo 7 (Filme)
    ('Série', 8, 8);   -- Ator 8 participa no Conteúdo 8 (Série)
    
    
INSERT INTO assistidos (
    assistidos_avaliacao,
    assistidos_id_tipo,
    assistidos_id_cliente
) VALUES
    (4, 1, 1),  -- Avaliação 4 para o tipo de conteúdo 1 (por exemplo, Filme) por cliente 1
    (5, 2, 2),  -- Avaliação 5 para o tipo de conteúdo 2 (por exemplo, Série) por cliente 2
    (3, 3, 3),  -- Avaliação 3 para o tipo de conteúdo 3 (por exemplo, Documentário) por cliente 3
    (2, 1, 4),  -- Avaliação 2 para o tipo de conteúdo 1 (por exemplo, Filme) por cliente 4
    (4, 2, 5),  -- Avaliação 4 para o tipo de conteúdo 2 (por exemplo, Série) por cliente 5
    (1, 3, 6),  -- Avaliação 1 para o tipo de conteúdo 3 (por exemplo, Documentário) por cliente 6
    (5, 1, 7),  -- Avaliação 5 para o tipo de conteúdo 1 (por exemplo, Filme) por cliente 7
    (3, 2, 8);  -- Avaliação 3 para o tipo de conteúdo 2 (por exemplo, Série) por cliente 8
    
    INSERT INTO temporada (temporada_nome_da_temporada) VALUES
('Primavera 2024'),
('Verano 2024'),
('Otoño 2024'),
('Invierno 2024'),
('Primavera 2025'),
('Verano 2025'),
('Otoño 2025'),
('Invierno 2025');



    

    
    


    
    
















 