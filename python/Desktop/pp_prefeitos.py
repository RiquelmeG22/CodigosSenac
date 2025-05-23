import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pp_prefeitos.csv')

plt.title('Vereadores Eleitos CG')

data = df.loc[:,['Nome', 'Voto']]

print(len(data))

ep = [0.1 if i != 0 else 0.3 for i in range(len(data))]

plt.pie(data.iloc[:, 1], labels=data.iloc[:, 0], explode=ep,autopct='%.2f%%')
plt.show()

plt.barh(data['Nome'], data['Voto'], color='blue')

plt.xlabel('Voto')
plt.ylabel('Vereadores')
plt.tight_layout()


plt.show()

