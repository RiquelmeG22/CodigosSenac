base = float(input('Digite a base '))
exp = int(input('Digite um expoente '))

result = 1

for i in range(exp):
    result *= base


print(result)
