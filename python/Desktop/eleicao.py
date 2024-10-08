# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('eleicao.csv')
# #df.set_index('Posição', inplace=True)



# plt.title('Vereadores Eleitos CG')

# data = df.loc(['Nome', 'Votos'])
# print(len(data))

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('eleicao.csv')

plt.title('Vereadores Eleitos CG')

data = df.loc[['Nome', 'Voto']]

print(len(data))


plt.barh(data['Nome'], data['Voto'], color='blue')

plt.xlabel('Voto')
plt.ylabel('Vereadores')
plt.tight_layout()


plt.show()
