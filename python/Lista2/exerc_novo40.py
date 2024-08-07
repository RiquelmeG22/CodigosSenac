saltHour = float(input('Digite o salário por hora: '))
hours = float(input('Digite a quantidade de horas trabalhadas: '))

saltFull = saltHour * hours
ir = saltFull * 0.11
inss = saltFull * 0.08
sinc = saltFull * 0.05

print(f'Salário bruto: {saltFull:.2f} \nINSS: {inss:.2f} \nSindicato: {sinc:.2f} \nSalário líquido: {saltFull - inss - ir - sinc:.2f}')