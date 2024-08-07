#Escreva uma função que recebe um valor em horas e retorna o equivalente em minutos

def hora_min(horas):
    minutos = horas * 60
    return minutos
    
horas = 4
min = hora_min(horas)
print(f'{horas} horas são {min} minutos. ')


