num = int(input('Digite um número inteiro'))
preco = num * .95
print(f'O valor da blusa é {num} com desconto ela fica por {preco:.2f} ')

n = int(input('Digite um numero para ver o valor da tabuada'))
print(f' O valor da tabuada é {n} x 2 = {n*2}')

def triangulos(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não é possível formar um triângulo com esses valores"

# Solicita ao usuário para inserir os valores dos lados do triângulo
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Chama a função verificar_triangulo e imprime o resultado
resultado = triangulos(a, b, c)
print(resultado)
