populacaoA = 0
while(populacaoA <=0):
    populacaoA = int(input('Digite a populaçao inicial:pais A '))

growtA = 0.
while(growtA <= 0):
    growtA = float(input('Digite o crescimento do valor A: '))    
populacaoB = 0.
while(populacaoB <= 0):
    populacaoB = int(input('Digite a população inicial: pais B'))
growtB = 0.
while(growtB <=0):
    growtB = float  (input('Digite o crescimento do pais B: '))  
counter = 0

if(populacaoA < populacaoB):
    while(populacaoA <= populacaoB):
        populacaoA = int(populacaoA * (1 + growtA))
        populacaoB = int(populacaoB * (1 + growtB))
        counter += 1
    else:
        print(f'Anos necessarios: {counter}, População pais A: {int(populacaoA)} e populacao pais B: {int(populacaoB)} ')

    
