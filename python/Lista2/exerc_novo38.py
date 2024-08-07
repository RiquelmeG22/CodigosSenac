mass = float(input('Digite sua massa: '))
height = float(input('Digite sua altura: '))

imc = mass / (height * height)

if(imc <= 18.5):
    print('Abaixo do peso')
elif(imc < 25.):
    print('Saudável')
elif(imc < 30.):
    print('Peso em excesso')
elif(imc < 35.):
    print('Obesidade Grau I')
elif(imc < 40.):
    print('Obesidade Grau II')
elif(imc < 50.):
    print('Obesidade Grau III')
else:
    print('Obesidade Grau Burano Negro')