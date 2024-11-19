import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('rj_prefeitos.csv')

plt.title('Prefeitos no Rio de Janeiro')


data = df.loc[:, ['Nome', 'Partido', 'Votos']]


print(len(data))


ep = [0.1 if i != 0 else 0.3 for i in range(len(data))]


plt.figure(figsize=(8, 8))  
plt.pie(data['Votos'], labels=data['Nome'], explode=ep, autopct='%.2f%%')
plt.show()

plt.figure(figsize=(10, 6)) 
plt.barh(data['Nome'], data['Votos'],color='blue') 

plt.xlabel('Votos')
plt.ylabel('Prefeitos')
plt.tight_layout()

plt.show()

