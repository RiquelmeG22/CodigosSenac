num = int(input('Digite um numero '))
salario = num*40.5
if salario >2.500:
    print(f'Slario liquido {salario * 0.89:.2f} R$, COM {salario * .11:.2f} R$ de imposto de renda ')
else:
    print(f'Salário liquído {salario:.2f} R$')    