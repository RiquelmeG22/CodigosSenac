while True:
    nome = input('Digite seu nome completo ').title()
    senha = input('Digite sua senha ')
    if senha !=  nome:
        print('Cadastrado com sucesso ')
        break
    else:
        print('A senha não pode ser igual o nome ')