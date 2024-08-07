class Pessoa:
    nome = ''
    idade = ''
    peso = ''
    altura = ''
    sexo = ''

    def setNome(self, nome: str):
        self.nome = nome
        return self.nome
    def setidade(self, idade: int):
        self.idade = idade
        return self.idade
    def setpeso(self, peso: float):
        self.peso = peso
        return self.peso
    def setaltura(self, altura: float):
        self.altura = altura
        return self.idade
    def setsexo(self, sexo: str):
        self.sexo = sexo
        return self.sexo
    
class trabalhador(Pessoa):
    salario = ''
    anos_trabalhados = ''

    def setsalario(self, salario: float):
        self.salario = salario
        return self.salario
    def setanos_trabalhados(self, anos_trabalhados: int):
        self.anos_trabalhados = anos_trabalhados
        return self.anos_trabalhados

senac = trabalhador()

senac.setsalario(float(input('Digite seu salario: ')))
senac.setanos_trabalhados(int(input('Digite os anos trabalhados: ')))
senac.setaltura(float(input('Digite sua altura: ')))

print(senac.salario)


riquelme = Pessoa()

riquelme.setNome(input('Digite seu nome:'))
riquelme.setidade(int(input('Digite sua idade:')))
riquelme.setpeso(float(input('Digite seu peso: ')))
riquelme.setaltura(float(input('Digite sua altura: ')))
riquelme.setsexo(str(input('Digite seu sexo: ')))

print(riquelme.nome)


class Estudante(Pessoa):
    turma = ''
    colegio = ''

    def setturma(self, turma: int):
        self.turma = turma
        return self.turma
    def setcolegio(self, colegio: str):
        self.colegio = colegio
        return self.colegio
    
rj = Estudante()

rj.setturma(int(input('Digite sua turma: ')))
rj.setcolegio(input('informe o nome do seu colégio: '))


print(rj.turma)
print(rj.colegio)




