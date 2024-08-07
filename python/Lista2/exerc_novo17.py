aprovar_emprestimo(salario, prestacao):
limite_prestacao = salario * 0.20  # 20% do salário

if prestacao > limite_prestacao:
    return "Empréstimo não concedido"
else:
    return "Empréstimo concedido"

# Entrada de dados
salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

# Verificação e impressão do resultado
print(aprovar_emprestimo(salario, prestacao))
