# Atividade (17/10)
# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, representando subdivisões até chegar a classes específicas como Ornitorrinco, Morcego e Baleia.
 
# Criação das Classes Principais:
 
# Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
# Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
# Características Específicas:
 
# Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
# Mamíferos: método amamentar().
# Aves: método voar().
# Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
# Atributos e Métodos:
 
# Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
# Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes).
# """


class Animal:
    def __init__(self, nome_cientifico, cor) -> None:
        self.nome_cientifico = nome_cientifico
        self.cor = cor

    def comer(self):
        print(f'O animal {self.nome_cientifico}: nhame nhame')

    def respira(self):
        print(f"O animal {self.nome_cientifico}: zzzzzz")

    def movimenta(self):
        print(f"O animal {self.nome_cientifico}: shishsihsia")

    
class Vertebrado(Animal):
    def __init__(self, nome_cientifico, cor, ambiente) -> None:
        super().__init__(nome_cientifico, cor)
        self.ambiente = ambiente

    def reproducao(self):
        print(f"O animal {self.nome_cientifico}: tem filhotes")


class Mamifero(Vertebrado):
    def __init__(self, nome_cientifico, cor, ambiente, raca) -> None:
        super().__init__(nome_cientifico, cor, ambiente)
        self.raca = raca
    def amamenta(self):
        print(f"O animal {self.nome_cientifico} amamenta")

class Repties(Mamifero):
    def __init__(self, nome_cientifico, cor, ambiente, raca, escama) -> None:
        super().__init__(nome_cientifico, cor, ambiente, raca)
        self.escama = escama

    def nada(self):
        print(f"O animal {self.nome_cientifico}: nada")

class Baleia(Repties):
    def __init__(self, nome_cientifico, cor, ambiente, raca, escama, tamanho) -> None:
        super().__init__(nome_cientifico, cor, ambiente, raca, escama)
        self.tamanho = tamanho

    def comprimento(self):
        print(f"A altura do animal é {self.tamanho}")


class Morcego(Baleia):
    def __init__(self, nome_cientifico, cor, ambiente, raca, escama, tamanho, carnivoro) -> None:
        super().__init__(nome_cientifico, cor, ambiente, raca, escama, tamanho)
        self.carnivoro = carnivoro
    
    def comer(self):
        if self.carnivoro:
            print(f"O morcego {self.nome_cientifico} come carne")
        else:
            print(f"O morcego {self.nome_cientifico} come fruta")

class Onitorinco(Morcego):
    def __init__(self, nome_cientifico, cor, ambiente, raca, escama, tamanho, carnivoro, bota) -> None:
        super().__init__(nome_cientifico, cor, ambiente, raca, escama, tamanho, carnivoro)
        self.bota = bota

    def ovo(self):
        print(f"O animal {self.nome_cientifico} bota ovo!")



