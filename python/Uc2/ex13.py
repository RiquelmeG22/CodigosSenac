
#Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é 
#uma palavra ou frase que se lê da mesma forma de trás para frente. Por exemplo, “arara” é 
#um palíndromo.



def palindromo(text):
    text = text.replace(' ', '').lower()
    return text == text [::-1]

frase = input('Digite uma palavra ou uma frase ')

if palindromo(frase):
    print('É um palíndromo!!')
else:
    print('Não é um palíndromo!! ')