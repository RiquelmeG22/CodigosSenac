matricula = ''
altura = 0
fisico = 1
sexo = ''
falta = 0
mTotal = 0
mbom = 0
 


matricula = input('Informe a matricula do aluno')
while matricula != '0':
    while True:
        sexo = input('Digite o sexo do aluno(a), M ou F:')
        if sexo == 'M' or sexo == 'F':
            break
    altura = int(input('Digite a altura do aluno')) 
    while True:
        fisico = int(input('Digite o fisico do aluno 1-bom, 2-regular, 3-ruim: '))
        if fisico == 1 or fisico == 2 or fisico == 3:
            break
    if sexo == 'F' and altura > 170:
        falta += 1
    if sexo == 'M' and fisico == 1:
        mbom += 1
    if sexo == 'M':
        mTotal += 1
    matricula = input('Digite a matricula do aluno:')    

    print(f'A quantidade de alunas com mais de 170cm é: {falta} \nB)A porcentagem de alunos com fisico bom é: {round(mbom/mTotal, 2)}')


    



    



