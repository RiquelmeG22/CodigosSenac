total = 0.
price = -1.0
counter = 1

while True:
    while(price != 0.):
        price = float(input('Produto {}: R$ '.format(counter)))
        total += price
        counter += 1
    print(f'Total: R$ {total:.2f}')

    cash = float(input('Dinheiro: R$ '))

    exchange = cash - total
    print(f'Troco: R$ {exchange:.2f}')
    counter = 1
    price = -1.
    total = 0.