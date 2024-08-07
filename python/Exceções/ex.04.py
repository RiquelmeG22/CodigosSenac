numero = [num for num in range(1, 11)]


try:
    idx = int(input('Digite um número de 1 a 10: '))
    idx -= 1
    print(f'Seu número é {numero[idx]} ')
except IndexError as e:
    print(f'Digite um número de 1 a 10! {e} ')
except ValueError as e:
    print(f'Digite um número inteiro! {e} ')