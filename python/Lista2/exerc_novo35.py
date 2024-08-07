vendas = float(input('Digite o valor da venda em mil '))
if vendas >=100:
    print(f'A sua comisão de venda é {vendas*1000*0.16+700} ')
elif vendas >=80:
    print(f'A sua comisão de venda é {vendas*1000*0.14+650} ')  
elif vendas >=60:
    print(f'A sua comisão de venda é {vendas*1000*0.14+600} ')  
elif vendas >= 40:
    print(f'A sua comisão de venda é {vendas*1000*0.14+550} ') 
elif vendas >= 20:
      print(f'A sua comisão de venda é {vendas*1000*0.14+500} ') 
elif vendas <20:
    print(f'A sua comisão de venda é {vendas*1000*0.14+400} ') 


