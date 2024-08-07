total = 0
ingressos = []
 
while True:
    nome = input("Digite o nome da pessoa (ou digite 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
 
    valor = float(input("Digite o valor do ingresso: "))
    tipo = input("Digite o tipo do ingresso (meia ou inteira): ").lower()
 
    if tipo == "meia":
        carteirinha = input("Você possui carteirinha de estudante? (s/n): ").lower()
        if carteirinha == "s":
            ingressos.append((nome, "meia com carteirinha"))
            total += valor / 2
        else:
            ingressos.append((nome, "meia"))
            print("É necessário possuir carteirinha para comprar o ingresso com desconto.")
    elif tipo == "inteira":
        ingressos.append((nome, "inteira"))
        total += valor
    else:
        print("Tipo de ingresso inválido!")
 
print("\nIngressos comprados:")
for ingresso in ingressos:
    print(f"{ingresso[0]} - {ingresso[1]}")
 
print(f"\nValor total da compra: R${total:.2f}")



