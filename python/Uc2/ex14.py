
def vogais(text):
    return sum(text.count(vowel) for vowel in 'aeiouAEIOU ') 

string = input('Digite uma palavra: ')
print(f'Essa frase tem {vogais(string)} vogais ')
    
 
