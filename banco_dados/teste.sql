CREATE DATABASE teste;
USE teste;

-- Tabelas sem referências externas
CREATE TABLE transportadoras (
  id_transp INT NOT NULL AUTO_INCREMENT,
  nome_transp VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (id_transp)
);

CREATE TABLE situacao_icms (
  id_st_icms INT NOT NULL AUTO_INCREMENT,
  st_icms INT DEFAULT NULL,
  descricao_icms VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (id_st_icms)
);

CREATE TABLE situacao_cadastro (
  id_st_cadastro INT NOT NULL AUTO_INCREMENT,
  st_cadastro VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (id_st_cadastro)
);

CREATE TABLE sexos (
  id_sexo INT NOT NULL AUTO_INCREMENT,
  sexo VARCHAR(46) DEFAULT NULL,
  PRIMARY KEY (id_sexo)
);

CREATE TABLE produto (
  id_produto INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(255) DEFAULT NULL,
  variante VARCHAR(100) DEFAULT NULL,
  p_s VARCHAR(255) DEFAULT NULL,
  codigo INT DEFAULT NULL,
  qtde_base INT DEFAULT NULL,
  qtde INT DEFAULT NULL,
  um VARCHAR(50) DEFAULT NULL,
  custo_unitario FLOAT DEFAULT NULL,
  custo_total FLOAT DEFAULT NULL,
  qtde_fixa_variavel FLOAT DEFAULT NULL,
  ordem VARCHAR(100) DEFAULT NULL,
  c_i VARCHAR(100) DEFAULT NULL,
  origem VARCHAR(255) DEFAULT NULL,
  status_produto VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (id_produto)
);

-- Criação da tabela cliente, que será referenciada por outras tabelas
CREATE TABLE cliente (
  id_cliente INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  email VARCHAR(100) DEFAULT NULL,
  email_danfe VARCHAR(100) DEFAULT NULL,
  email_cobranca VARCHAR(100) DEFAULT NULL,
  email_loja_virtual VARCHAR(100) DEFAULT NULL,
  telefone_comercial VARCHAR(20) DEFAULT NULL,
  ramal VARCHAR(9) DEFAULT NULL,
  telefone_residencial VARCHAR(20) DEFAULT NULL,
  telefone_celular VARCHAR(20) DEFAULT NULL,
  fax VARCHAR(50) DEFAULT NULL,
  cpf VARCHAR(11) NOT NULL,
  rg VARCHAR(7) NOT NULL,
  id_recomendador INT DEFAULT NULL,
  endereco VARCHAR(255) DEFAULT NULL,
  situacao_icms INT DEFAULT NULL,
  inscricao_estadual VARCHAR(9) DEFAULT NULL,
  inscricao_suframa VARCHAR(50) DEFAULT NULL,
  sexo INT DEFAULT NULL,
  data_nascimento DATE DEFAULT NULL,
  transportadora_1 INT DEFAULT NULL,
  transportadora_2 INT DEFAULT NULL,
  tabela_preco INT DEFAULT NULL,
  mod_frete_padrao VARCHAR(50) DEFAULT NULL,
  situacao_cadastro INT DEFAULT NULL,
  linha_peef VARCHAR(50) DEFAULT NULL,
  aliquota FLOAT DEFAULT NULL,
  PRIMARY KEY (id_cliente),
  KEY id_recomendador (id_recomendador),
  KEY sexo (sexo),
  KEY situacao_icms (situacao_icms),
  KEY transportadora_1 (transportadora_1),
  KEY transportadora_2 (transportadora_2),
  KEY situacao_cadastro (situacao_cadastro),
  -- Removido KEY tabela_preco (tabela_preco),
  CONSTRAINT cliente_ibfk_1 FOREIGN KEY (id_recomendador) REFERENCES cliente (id_cliente),
  CONSTRAINT cliente_ibfk_2 FOREIGN KEY (sexo) REFERENCES sexos (id_sexo),
  CONSTRAINT cliente_ibfk_3 FOREIGN KEY (situacao_icms) REFERENCES situacao_icms (id_st_icms),
  CONSTRAINT cliente_ibfk_4 FOREIGN KEY (transportadora_1) REFERENCES transportadoras (id_transp),
  CONSTRAINT cliente_ibfk_5 FOREIGN KEY (transportadora_2) REFERENCES transportadoras (id_transp),
  CONSTRAINT cliente_ibfk_6 FOREIGN KEY (situacao_cadastro) REFERENCES situacao_cadastro (id_st_cadastro)
  -- Removido CONSTRAINT cliente_ibfk_7 FOREIGN KEY (tabela_preco) REFERENCES precos (id_tb_preco)
);

-- Tabelas que referenciam a tabela cliente
CREATE TABLE precos (
  id_tb_preco INT NOT NULL AUTO_INCREMENT,
  id_produto INT DEFAULT NULL,
  preco FLOAT DEFAULT NULL,
  id_vendedor INT DEFAULT NULL,
  PRIMARY KEY (id_tb_preco),
  KEY id_produto (id_produto),
  KEY fk_vendedor (id_vendedor),
  CONSTRAINT fk_vendedor FOREIGN KEY (id_vendedor) REFERENCES cliente (id_cliente),
  CONSTRAINT precos_ibfk_1 FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE ordem_servico (
  id_ordem_servico INT NOT NULL AUTO_INCREMENT,
  documento TEXT,
  emissao DATE DEFAULT NULL,
  id_cliente INT DEFAULT NULL,
  previsao DATE DEFAULT NULL,
  descricao TEXT,
  execucao VARCHAR(255) DEFAULT NULL,
  servico VARCHAR(255) DEFAULT NULL,
  variante VARCHAR(100) DEFAULT NULL,
  quantidade FLOAT DEFAULT NULL,
  valor FLOAT DEFAULT NULL,
  PRIMARY KEY (id_ordem_servico),
  KEY id_cliente (id_cliente),
  CONSTRAINT ordem_servico_ibfk_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE nf_venda_peca (
  id_nf_venda_peca INT NOT NULL AUTO_INCREMENT,
  documento TEXT,
  sequencia INT DEFAULT NULL,
  emissao DATE DEFAULT NULL,
  vencimento DATE DEFAULT NULL,
  previsao_faturamento FLOAT DEFAULT NULL,
  aprovacao_cliente DATE DEFAULT NULL,
  hr_aprovacao VARCHAR(50) DEFAULT NULL,
  embarque INT DEFAULT NULL,
  prazo_entrega DATE DEFAULT NULL,
  n_pedido_compra INT DEFAULT NULL,
  id_vendedor INT DEFAULT NULL,
  id_cliente INT DEFAULT NULL,
  end_entrega VARCHAR(255) DEFAULT NULL,
  tb_preco INT DEFAULT NULL,
  transportadora_1 INT DEFAULT NULL,
  transportadora_2 INT DEFAULT NULL,
  tipo_frete VARCHAR(50) DEFAULT NULL,
  valor_frete FLOAT DEFAULT NULL,
  porcentagem FLOAT DEFAULT NULL,
  valor_desconto_rateado FLOAT DEFAULT NULL,
  contato VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (id_nf_venda_peca),
  KEY id_cliente (id_cliente),
  KEY transportadora_1 (transportadora_1),
  KEY transportadora_2 (transportadora_2),
  KEY id_vendedor (id_vendedor),
  KEY tb_preco (tb_preco),
  CONSTRAINT nf_venda_peca_ibfk_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
  CONSTRAINT nf_venda_peca_ibfk_2 FOREIGN KEY (transportadora_1) REFERENCES transportadoras (id_transp),
  CONSTRAINT nf_venda_peca_ibfk_3 FOREIGN KEY (transportadora_2) REFERENCES transportadoras (id_transp),
  CONSTRAINT nf_venda_peca_ibfk_4 FOREIGN KEY (id_vendedor) REFERENCES cliente (id_cliente),
  CONSTRAINT nf_venda_peca_ibfk_5 FOREIGN KEY (tb_preco) REFERENCES precos (id_tb_preco)
);

CREATE TABLE login (
  user_name VARCHAR(50) DEFAULT NULL,
  password VARCHAR(50) DEFAULT NULL,
  id_cliente INT DEFAULT NULL,
  KEY id_cliente (id_cliente),
  CONSTRAINT login_ibfk_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);