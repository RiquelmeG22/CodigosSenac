
class Livros():
    def __init__(self, titulo, autor, genero, cod_livro) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

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




    

















