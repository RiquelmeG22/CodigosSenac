def comission(fabric: float) -> float:
    if(fabric < 12_000.):
        return fabric * 0.05
    elif(fabric <= 25_000.):
        return fabric * 0.1
    else:
        return fabric * 0.15

def tax(fabric: float) -> float:
    if(fabric < 12_000.):
        return 0.
    elif(fabric <= 25_000.):
        return fabric * 0.15
    else:
        return fabric * 0.2

price = float(input('Digite o preço de fabrica do carro: '))

print(price + price*.25)

print(f'Valor final a pagar: {price + comission(price) + tax(price):.2f}')