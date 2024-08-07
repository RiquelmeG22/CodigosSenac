salario = float(input('Digite o seu salario '))
tds = float(input('Digite o tempo de serviço trabalhado '))
snovo = 0
if salario <=500:
    snovo = salario + salario *0.25
elif salario <=1000:
    snovo = salario + salario *0.20
elif salario <=1500:
    snovo = salario + salario *0.15
elif salario <=2000:
    snovo = salario + salario *0.10
elif salario >2000:
    snovo = salario + salario *0

if tds <1:
    snovo += 0
elif tds <4:
    snovo +=100
elif tds <7:
    snovo +=200
elif tds <11:
    snovo +=300
elif tds >10:
    snovo +=500

if snovo == salario:
    print('Não tem direito a nada ')

print(f'O salario final é {snovo} ')    
    
    



    
    
        
