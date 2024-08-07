tempo_minutos = int(input('Digite a quantidade de tempo em minutos')) 
if tempo_minutos < 15:
    print('Estacioamento é gratis')    
else:
    horas = tempo_minutos / 60
    valor_total = 9
    if horas > 1:
        valor_total += (horas-1) *1.5
    print(f'Valor total a ser cobrado: R$ {valor_total}')

             
    

