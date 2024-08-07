number = int(input('Digite um valor'))
soma = 0
quantidade = 1
while number>0 and number<50:
    soma = soma + number
    number = int(input('Digite um valor'))
    quantidade+=1

print(f'O resultado é {soma} a quantidae de números é {quantidade}')    
