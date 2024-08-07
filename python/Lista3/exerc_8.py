salt = 1000.
growth = 0.015

while(True):
    salt *= 1 + growth

    year = int(input('Digite o ano atual: '))
    while(year <= 1996):
        year = int(input('Digite o ano atual: '))

    for i in range(year - 1996):
        growth *= 2
        print(growth)
        salt *= 1 + growth
    print(f'Salário final: {salt:.2f}')
    salt = float(input('Digite um novo salário inicial: '))
    growth = float(input('Digite a txa de crescimento incial: '))