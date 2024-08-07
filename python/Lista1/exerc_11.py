name = ''
age = 0
income = 0
sex = ''

while len(name) <= 3:
    name = input('Digite seu nome')
while age <= 0 or age> 150:
    age = int(input('Digite sua idade'))
while income <= 0:
    income = float(input('Digite seu salario'))
while not(sex == 'M' or sex == 'F'):
    sex = input('Digite seu sexo')
print(f'O meu {name.title()} e eu tenho {age} recebo um valor de {income} e sou {sex}')    

