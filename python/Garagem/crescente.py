
lista = list(map(int, input("Digite os números separados por espaço: ").split()))


n = len(lista)

for i in range(n - 1):
  
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
        
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


print("Lista ordenada:", lista)
