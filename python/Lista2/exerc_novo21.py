lab = -1.0
sem = -1.0
final = -1.0

while lab < 0.0 or lab > 10.0:
    lab = float(input('Digite a nota do lab entre 0 a 10 ')) 

while sem < 0.0 or sem > 10.0:
    sem = float(input('Digite a nota do lab entre 0 e 10'))

while final < 0.0 or final > 10.0:
    final = float(input('Digite a nota do lab entre 0 e 10'))    

media = (lab * 2 + sem * 3 + final * 5) /10
print(media)

if media <= 2.9:
    print('reprovado')
elif media <= 5.9:
    print('Recuperação')
else:
    print('Aprovado')        

     