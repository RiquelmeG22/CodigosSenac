maior = None
menor = None

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
        
print(f"O maior número informado é: {maior}")
print(f"O menor número informado é: {menor}")
