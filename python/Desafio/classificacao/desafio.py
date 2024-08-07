


class Reino:
    def __init__(self, reino: str):
        super().__init__(reino)
        self.reino = reino
        return super().__str__() + f', Reino: {self.reino}'

class Filo(Reino):
    def __init__(self, reino: str, filo: str):
        super().__init__(reino, filo)
        self.filo = filo
        return super().__str__() + f', Filo: {self.filo}'

class Classe(Filo):
    def __init__(self, reino: str, filo: str, classe: str):
        super().__init__(reino, filo, classe)
        self.classe = classe
        return super().__str__() + f', Classe: {self.classe}'

class Ordem(Classe):
    def __init__(self, reino: str, filo: str, classe: str, ordem: str):
        super().__init__(reino, filo, classe, ordem)
        self.ordem = ordem
        return super().__str__() + f', Ordem: {self.ordem}'

class Familia(Ordem):
    def __init__(self, reino: str, filo: str, classe: str, ordem: str, familia: str):
        super().__init__(reino, filo, classe, ordem, familia)
        self.familia = familia 
        return super().__str__() + f', Familia: {self.familia}'

class Genero(Familia):
    def __init__(self, reino: str, filo: str, classe: str, ordem: str, familia: str, genero: str):
        super().__init__(reino, filo, classe, ordem, familia, genero)
        self.genero = genero
        return super().__str__() + f', Genero: {self.genero}'

class Especie(Genero):
    def __init__(self, reino: str, filo: str, classe: str, ordem: str, familia: str, genero: str, especie: str):
        super().__init__(reino, filo, classe, ordem, familia, genero, especie)
        self.especie = especie
        return super().__str__() + f', Especie: {self.especie}'

class Animal(Especie):
    def __init__(self, reino: str, filo: str, classe: str, ordem: str, familia: str, genero: str, especie: str, animal: str):
        super().__init__(reino, filo, classe, ordem, familia, genero, especie, animal)
        self.animal = animal
        return super().__str__() + f', Animal: {self.animal}'
    

    
gato = Animal('Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Felídeos', 'Felis')

    


