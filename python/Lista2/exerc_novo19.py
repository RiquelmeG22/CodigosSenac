def soma_algarismos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10  # Obtém o último algarismo e adiciona à soma
        numero //= 10  # Remove o último algarismo do número
    return soma

numero = int(input("Digite um número inteiro maior que zero: "))

if numero > 0:
    resultado = soma_algarismos(numero)
    print(f"A soma dos algarismos de {numero} é {resultado}.")
else:
    print("Número inválido.")
