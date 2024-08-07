def ceil(num: float) -> int:
    aux = (num * 10) // 1
    if( aux % 10 > 0):
        aux = num // 1
        aux += 1
    return int(aux)


area = float(input('Digite a área a pintar em m²: '))

liters = area / 6

canBig = liters // 18
print((liters % 18.0) / 3.6)
cansmall = ceil((liters % 18.0) / 3.6)

print(f'Valor a pagar por {canBig} latas grandes e {cansmall} latas pequenas é: {canBig * 80.0 + cansmall * 25.}')