
cargo = input("Digite o cargo: ")
nome = input("Digite o nome completo: ")
idade = int(input("Digite a idade: "))
qualificacao = input("Possui qualificação na área? (S/N): ").upper()

if idade < 18:
    print('Parabéns voce foi aprovado para a proxima fase.')
else:
    print('Voce não passou para a proxima etapa.')
    exit()
qualificacao = input('Possui qualificação na área? (S/N): ')
if qualificacao == 'S':
    print('parabéns voce passou para a proxima fase' )
else:
    print('Voce não passou para a proxima fase ')
    exit()
nota = float(input('Digite a nota do conhecimento específico: '))
if nota > 7:
    print('Parabéns, voce foi aprovado para a proxima etapa do processo seletivo.' )
else:
    print('Infelizmennte, sua nota não foi suficiente para avancar para a próxima etapa. ')

