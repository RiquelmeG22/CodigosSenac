class Usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self, nome, cpf, telefone) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de emprestimos antigido!!'
        
    
        self.lista_livros.append(livro.nome)
