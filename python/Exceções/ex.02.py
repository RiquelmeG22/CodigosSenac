class Divisao():
    def __init__(self, num = float, den = float) -> None:
        self.num = num
        self.den = den
        self.result = num/den
        def resultado(self) -> float:
            return self.result

try:
    dev = Divisao(float(input('Digite o numerador: ')), float(input('Digite o denominador: ')))
    print(f'Resultado da divisão de {dev.num} por {dev.den} é {dev.result:.2f} ')
except ValueError as e:
    print(f'Digite um número {e} ')
except ArithmeticError as e:
    print(f'O denominador não pode ser zero {e} ')
        
        
