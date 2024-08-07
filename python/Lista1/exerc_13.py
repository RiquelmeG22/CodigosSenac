entrada = []
soma = 0

for i in range(20):
    entrada.append(int(input('Digite um numero')))
for i in range(20):
    if entrada[i]>0: 
        soma = soma + entrada[i]   
        print(f'A soma dos positivos é {soma}')
for i in range(20):
    if entrada[i]<0:
        print(f'Os números negativos são {entrada[i]}')

    
    
