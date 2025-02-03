
n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

termo1 = 0
termo2 = 1


if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print(f"Sequência de Fibonacci: {termo1}")
else:
  
    print("Sequência de Fibonacci:")
    print(termo1, end=" ")
    print(termo2, end=" ")

    for i in range(2, n):
        proximo_termo = termo1 + termo2
        print(proximo_termo, end=" ")
        
        termo1 = termo2
        termo2 = proximo_termo
