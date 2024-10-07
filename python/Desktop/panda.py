import pandas as pd

print(pd.__version__)

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#print(df.head())

#print(df.head())  selecionar os 5 primeiros 

#print(df.info()) mostra os dados dos elementos 

#print(df.set_index('PassengerId')) 

#print(df.values)

#print(df.loc[[1,2], ['Name','Sex','Age']])

#print(df.loc[10:20]) fatiamento entre os numeros

#print(df.loc[10:20:2]) pega de 2 em 2 se deixar vazio ele vai do 10 ate o final 

#print(df.loc[1:10, ['Name','Sex','Age']]) os registro de 1 ate o 10 trazendo as inf name sex age

#print(df.query('Age > 20').head())

#print(df.query('Age > 20'))

#print(df.query('Age >20 & Sex=="male"').head) seleciona todos maior q 20 anos e masculino

df.to_csv('dataset.csv', sep=',' , index=False, encoding='utf-8=sig')
