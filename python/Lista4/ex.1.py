while True:
    nota = float(input('Digite sua nota de zero a dez '))
    if nota>= 0 and nota <=10:
        print(f'Nota Valida {nota}' )
        break
    else:
        print('Nota invalida por favor digite novamente ')

