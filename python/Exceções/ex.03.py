cores = {
    "vermelho": "01",
    "preto": "02",
    "amarelo": "03",
    "branco": "04",
    "verde": "05",
}


try:
    key = input(f'Digite a cor que deseja saber o valor em Hex: {', '.join(cores)} ')
    print(f'A cor digita é {cores[key]}')
except KeyError as e:
    print(f'A chave digitado não existe!! {e} ')
