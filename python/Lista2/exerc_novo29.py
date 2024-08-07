idade = int(input('Digite sua idade '))
svt = (int(input('Digite seu tempo de serviço trabalhado ')))

if idade <= svt:
    print('Aposentadoria reprovada por informações incorretas ')
elif idade >=65:
    print('Aposentadoria aprovada por idade')   
elif svt >=30:
    print('Aposentadoria aprovada pelo tempo trabalhado ')
elif svt <=30:
    print('Aposentadoria reprovada ')
elif idade >=60 and svt >=25:
    print('Aposentadoria aprovada ')



