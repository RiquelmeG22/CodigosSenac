
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_csv('eleicao.csv')

# Contando as ocorrências de cada partido
partido = df['Partido'].value_counts()

# Criando o gráfico de pizza

plt.pie(partido, labels=partido.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição dos Partidos')
plt.axis('equal')  # Para garantir que o gráfico seja circular

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_csv('eleicao.csv')

# Contando as ocorrências de cada partido
partido_counts = df['Partido'].value_counts()

# Criando o gráfico de barras horizontal
plt.figure(figsize=(10, 6))
partido_counts.plot(kind='line', color='skyblue')
plt.xlabel('Número de Votos')
plt.ylabel('Partido')
plt.title('Distribuição de Votos por Partido')
plt.grid(axis='x')

plt.show()
