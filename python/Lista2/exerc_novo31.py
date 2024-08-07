km = float(input('Digite a quantidade do Km percorido '))
litros = float(input('Digite a quantidade de litros de gasolina '))
consumo = km/litros

if consumo <8:
    print('Venda o carro!! ')
elif consumo >8 or consumo <=14:
    print('Economico ')
elif consumo >=15:
    print('Super Economico ')    

    
        

