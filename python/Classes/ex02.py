class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float, estadocivil: str):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.estadocivil = estadocivil

        

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, altura: float, peso: float, estadocivil: str, materia: str):
        super().__init__(nome, idade, altura, peso, estadocivil)
        self.materia = materia 




