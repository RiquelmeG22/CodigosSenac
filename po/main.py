from livros import Livros
from usuario import Usuario
from biblioteca import Biblioteca
import mysql.connector

conexao = mysql.connector.connect(
    host = '10.28.2.71',
    database = 'biblioteca',
    user = 'suporte',
    password = 'suporte'
)


cursor = conexao.cursor()

# cursor.execute('uptade')


cursor.execute('')

cursor.execute('uptade livro set titulo = "Avatar",autor = "Riq",genero = "Comedia",status = "Disponivel" where codigo = 123;')

cursor.execute('insert into livro(titulo, autor, genero, status, codigo) values("O pequeno principe", "Enzo", "Fantasia", "Disponivel", 123);')

conexao.commit()


print(vars(conexao))


rafaela = Usuario('Rafaela', '009-765-898-05', '6799760590')

# print(vars(rafaela))

rafaela = Usuario('Rafaela', '009-765-898-05', '6799760590')

dom_carrasco = Livros('Kekel', 'Machado de Asis', '0909', 1)
antares = Livros("Incidente em Antares", 'Erico Verissimo','32',2)
poliana = Livros('Poliana', 'Eleanor H. Porter','231',3)
monica = Livros('Almancao da turma da monica', 'Mauricio de Souza','525', 4)


rafaela.pegar_emprestado(dom_carrasco)
print(vars(rafaela))  


