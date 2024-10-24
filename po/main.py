from livros import Livros
from usuario import Usuario
from biblioteca import Biblioteca

rafaela = Usuario('Rafaela', '009-765-898-05', '6799760590')

# print(vars(rafaela))

rafaela = Usuario('Rafaela', '009-765-898-05', '6799760590')

dom_carrasco = Livros('Kekel', 'Machado de Asis', '0909', 1)
antares = Livros("Incidente em Antares", 'Erico Verissimo', 'Ficção Dispotica','32',2)
poliana = Livros('Poliana', 'Eleanor H. Porter', 'Literatura infantil', '231',3)
monica = Livros('Almancao da turma da monica', 'Mauricio de Souza','525', 4)


rafaela.pegar_emprestado(dom_carrasco)
print(vars(rafaela))  