
CREATE DATABASE biblioteca;


USE biblioteca;


CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,  
    nome VARCHAR(100),                          
    cpf VARCHAR(13),                            
    telefone VARCHAR(20)                    
);


CREATE TABLE livro (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,    
    titulo VARCHAR(50),                         
    autor VARCHAR(50),                          
    genero VARCHAR(50),                         
    status VARCHAR(50),                         
    isbn VARCHAR(50)                                  
);

CREATE TABLE emprestimo (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,  
    id_livro INT,                                 
    id_usuario INT,                               
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),   
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) 
);


INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES
('O Alquimista', 'Paulo Coelho', 'Aventura', 'disponível', 101),
('1984', 'George Orwell', 'Ficção científica', 'emprestado', 102),
('Dom Casmurro', 'Machado de Assis', 'Literatura Brasileira', 'disponível', 103),
('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 'reservado', 104);

INSERT INTO usuario (nome, cpf, telefone) VALUES
('João Silva', '12345678901', '987654321'),
('Maria Oliveira', '10987654321', '912345678'),
('Pedro Costa', '11223344556', '998877665'),
('Ana Pereira', '22334455667', '997788889');

