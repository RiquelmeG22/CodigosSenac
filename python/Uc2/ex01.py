
#Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma
#função retorna o valor da hipotenusa.




def hipo(ladoA, ladoB):
    return (ladoA * ladoA + ladoB * ladoB)** 0.5

a = float(input('Digite o lado A '))
b = float(input('Digite o lado B '))

print(f'Hipotenusa de {a:.2f} e {b:.2f} = {hipo(a, b):.2f}')