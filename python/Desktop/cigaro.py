import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cigaro.csv')


col = df.loc[:, ['Year', 'Age_Group', 'Gender', 'Smoking_Prevalence']]

genero = col.groupby('Gender')['Smoking_Prevalence'].mean()

plt.barh(genero.index, genero.values, color='purple')

plt.title('Prevalência de fumantes por gênero')
plt.xlabel('Porcentagem (%)')
plt.ylabel('Gênero')
plt.tight_layout()



plt.show()

