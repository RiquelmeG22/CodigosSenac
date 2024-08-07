
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))
resultado = ''
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        resultado = "Triângulo equilátero"
    elif a == b or a == c or b == c:
        resultado = "Triângulo isósceles"
    else:
        resultado ="Triângulo escaleno"
else:
    resultado = "Não é possível formar um triângulo com esses valores"
    
print(resultado)
