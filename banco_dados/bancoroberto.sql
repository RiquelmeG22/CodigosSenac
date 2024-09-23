CREATE TABLE `transportadoras` (
  `id_transp` int NOT NULL AUTO_INCREMENT,
  `nome_transp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_transp`)
);

CREATE TABLE `situacao_icms` (
  `id_st_icms` int NOT NULL AUTO_INCREMENT,
  `st_icms` int DEFAULT NULL,
  `descricao_icms` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_st_icms`)
);

CREATE TABLE `situacao_cadastro` (
  `id_st_cadastro` int NOT NULL AUTO_INCREMENT,
  `st_cadastro` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_st_cadastro`)
);

CREATE TABLE `sexos` (
  `id_sexo` int NOT NULL AUTO_INCREMENT,
  `sexo` varchar(46) DEFAULT NULL,
  PRIMARY KEY (`id_sexo`)
); 

CREATE TABLE `produto` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) DEFAULT NULL,
  `variante` varchar(100) DEFAULT NULL,
  `p_s` varchar(255) DEFAULT NULL,
  `codigo` int DEFAULT NULL,
  `qtde_base` int DEFAULT NULL,
  `qtde` int DEFAULT NULL,
  `um` varchar(50) DEFAULT NULL,
  `custo_unitario` float DEFAULT NULL,
  `custo_total` float DEFAULT NULL,
  `qtde_fixa_variavel` float DEFAULT NULL,
  `ordem` varchar(100) DEFAULT NULL,
  `c_i` varchar(100) DEFAULT NULL,
  `origem` varchar(255) DEFAULT NULL,
  `status_produto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_produto`)
);

CREATE TABLE `precos` (
  `id_tb_preco` int NOT NULL AUTO_INCREMENT,
  `id_produto` int DEFAULT NULL,
  `preco` float DEFAULT NULL,
  `id_vendedor` int DEFAULT NULL,
  PRIMARY KEY (`id_tb_preco`),
  KEY `id_produto` (`id_produto`),
  KEY `fk_vendedor` (`id_vendedor`),
  CONSTRAINT `fk_vendedor` FOREIGN KEY (`id_vendedor`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `precos_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`)
);

CREATE TABLE `ordem_servico` (
  `id_ordem_servico` int NOT NULL AUTO_INCREMENT,
  `documento` text,
  `emissao` date DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `previsao` date DEFAULT NULL,
  `descricao` text,
  `execucao` varchar(255) DEFAULT NULL,
  `servico` varchar(255) DEFAULT NULL,
  `variante` varchar(100) DEFAULT NULL,
  `quantidade` float DEFAULT NULL,
  `valor` float DEFAULT NULL,
  PRIMARY KEY (`id_ordem_servico`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `ordem_servico_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
);

CREATE TABLE `nf_venda_peca` (
  `id_nf_venda_peca` int NOT NULL AUTO_INCREMENT,
  `documento` text,
  `sequencia` int DEFAULT NULL,
  `emissao` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `previsao_faturamento` float DEFAULT NULL,
  `aprovacao_cliente` date DEFAULT NULL,
  `hr_aprovacao` varchar(50) DEFAULT NULL,
  `embarque` int DEFAULT NULL,
  `prazo_entrega` date DEFAULT NULL,
  `n_pedido_compra` int DEFAULT NULL,
  `id_vendedor` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `end_entrega` varchar(255) DEFAULT NULL,
  `tb_preco` int DEFAULT NULL,
  `transportadora_1` int DEFAULT NULL,
  `transportadora_2` int DEFAULT NULL,
  `tipo_frete` varchar(50) DEFAULT NULL,
  `valor_frete` float DEFAULT NULL,
  `porcentagem` float DEFAULT NULL,
  `valor_desconto_rateado` float DEFAULT NULL,
  `contato` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_nf_venda_peca`),
  KEY `id_cliente` (`id_cliente`),
  KEY `transportadora_1` (`transportadora_1`),
  KEY `transportadora_2` (`transportadora_2`),
  KEY `id_vendedor` (`id_vendedor`),
  KEY `tb_preco` (`tb_preco`),
  CONSTRAINT `nf_venda_peca_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `nf_venda_peca_ibfk_2` FOREIGN KEY (`transportadora_1`) REFERENCES `transportadoras` (`id_transp`),
  CONSTRAINT `nf_venda_peca_ibfk_3` FOREIGN KEY (`transportadora_2`) REFERENCES `transportadoras` (`id_transp`),
  CONSTRAINT `nf_venda_peca_ibfk_4` FOREIGN KEY (`id_vendedor`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `nf_venda_peca_ibfk_5` FOREIGN KEY (`tb_preco`) REFERENCES `precos` (`id_tb_preco`)
);

CREATE TABLE `login` (
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
);

CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `email_danfe` varchar(100) DEFAULT NULL,
  `email_cobranca` varchar(100) DEFAULT NULL,
  `email_loja_virtual` varchar(100) DEFAULT NULL,
  `telefone_comercial` varchar(20) DEFAULT NULL,
  `ramal` varchar(9) DEFAULT NULL,
  `telefone_residencial` varchar(20) DEFAULT NULL,
  `telefone_celular` varchar(20) DEFAULT NULL,
  `fax` varchar(50) DEFAULT NULL,
  `cpf` varchar(11) NOT NULL,
  `rg` varchar(7) NOT NULL,
  `id_recomendador` int DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `situacao_icms` int DEFAULT NULL,
  `inscricao_estadual` varchar(9) DEFAULT NULL,
  `inscricao_suframa` varchar(50) DEFAULT NULL,
  `sexo` int DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `transportadora_1` int DEFAULT NULL,
  `transportadora_2` int DEFAULT NULL,
  `tabela_preco` int DEFAULT NULL,
  `mod_frete_padrao` varchar(50) DEFAULT NULL,
  `situacao_cadastro` int DEFAULT NULL,
  `linha_peef` varchar(50) DEFAULT NULL,
  `aliquota` float DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `id_recomendador` (`id_recomendador`),
  KEY `sexo` (`sexo`),
  KEY `situacao_icms` (`situacao_icms`),
  KEY `transportadora_1` (`transportadora_1`),
  KEY `transportadora_2` (`transportadora_2`),
  KEY `situacao_cadastro` (`situacao_cadastro`),
  KEY `tabela_preco` (`tabela_preco`),
  CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`id_recomendador`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `cliente_ibfk_2` FOREIGN KEY (`sexo`) REFERENCES `sexos` (`id_sexo`),
  CONSTRAINT `cliente_ibfk_3` FOREIGN KEY (`situacao_icms`) REFERENCES `situacao_icms` (`id_st_icms`),
  CONSTRAINT `cliente_ibfk_4` FOREIGN KEY (`transportadora_1`) REFERENCES `transportadoras` (`id_transp`),
  CONSTRAINT `cliente_ibfk_5` FOREIGN KEY (`transportadora_2`) REFERENCES `transportadoras` (`id_transp`),
  CONSTRAINT `cliente_ibfk_6` FOREIGN KEY (`situacao_cadastro`) REFERENCES `situacao_cadastro` (`id_st_cadastro`),
  CONSTRAINT `cliente_ibfk_7` FOREIGN KEY (`tabela_preco`) REFERENCES `precos` (`id_tb_preco`));
