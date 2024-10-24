from livros import Livros
from usuario import Usuario

class Biblioteca:
    Acervo = []

    @staticmethod
    def emprestar(livro: Livros, usuario: Usuario):
        livro.EmprestarLivro(usuario)
        usuario.pegar_emprestado(livro)


    



