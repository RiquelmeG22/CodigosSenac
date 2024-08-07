name = ''
age = 0
income = 0
sex = ''
estadoc = ''

while len(name) <= 3:
    name = input('Digite seu nome')
while age <= 0 or age> 150:
    age = int(input('Digite sua idade'))
while income <= 0:
    income = float(input('Digite seu salario'))
while not(sex == 'M' or sex == 'F' or sex == 'O'):
    sex = input('Digite seu sexo')
while not(estadoc == 'C' or estadoc == 'S' or estadoc == 'V' or estadoc == 'D'):
    estadoc = input('Digite seu estado civil')  
print(f'O meu {name.title()} e eu tenho {age} recebo um valor de {income} e sou {sex} e meu estado civil é {estadoc}') 


