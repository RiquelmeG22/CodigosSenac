weightOver = 0.
fine = 0
fishWeight = float(input('Digite a massa do seu peixe em kg: '))

while fishWeight != 0:
    if fishWeight > 50.0:
        weightOver = fishWeight - 50.
        fine = weightOver * 4.
        print(f'Peso do peixe: {round(fishWeight, 2)}')

        if weightOver > 0:
            print(f'Peso acima do limite: {round(weightOver,1)} kg, multa a pagar: {round(fine, 1)} Reais')

        fishWeight = float(input('Digite a massa do peixe em kg: '))