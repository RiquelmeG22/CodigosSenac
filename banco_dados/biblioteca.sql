
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
    codigo INT                                  
);

CREATE TABLE emprestimo (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,  
    id_livro INT,                                 
    id_usuario INT,                               
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),   
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) 
);


SELECT * FROM livro;
