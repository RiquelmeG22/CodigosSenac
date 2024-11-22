
class Livros():
    def __init__(self, titulo, autor, genero, isbn) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        

        self.status = "Disponivel"
        self.usuario = None

    
    def EmprestarLivro(self, usuario):
        if self.status != "Disponivel":
            return 
        
        self.usuario = usuario
        self.status = 'Emprestado'


    def DevolverLivro(self):
        if self.status != "Emprestado":
            return 'Não pode ser devolvido!!'
        
        self.usuario = None
        self.status = "Disponivel"

    def castradarLivro(self):
        return 'INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES(%s,%s,%s,%s,%s)'

    def excluirLivro(self):
        return 'delete from usuario where id_usuario = 1;'
    
   


    # def deleteQuery(self):
    #     return 'delete from livro where isbn=%s'
    
    # def getIdLivroQuery(self):
    #     return 'update id_livro from livro where isbn=%s'   
    





    

















