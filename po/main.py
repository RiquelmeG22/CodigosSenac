from livros import Livros
from usuario import Usuario


rafaela = Usuario('Rafaela', '009-765-898-05', '6799760590')

print(vars(rafaela))

dom_carrasco = Livros('Kekel', 'Machado de Asis', '0909', 1)

print(vars(dom_carrasco))


rafaela.pegar_emprestado(dom_carrasco)
print(vars(rafaela))