usuario = input('Digite seu usario')
senha = input('Digite sua senha')

while True:
    senha = input('Digite sua senha diferente, do valor do usario')
    if senha.lower() != usuario.lower():
        print('Senha aceita')
        break
    print("A senha nao pode ser igual ao usuario")