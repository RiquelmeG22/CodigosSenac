#Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um
#quadrado de lado ‘n’ preenchido com hashtags. Por exemplo, para n=4, o resultado seria

def inv(num):
    print(('#' * num + '\n') * num)
    
n = int(input('Digite um número inteiro: '))

inv(n)

