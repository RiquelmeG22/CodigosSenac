
texto = input("Digite uma palavra ou frase: ")

texto_limpo = texto.replace(" ", "").lower()

if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
