import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("banco_dados/all_seasons.csv")
df.set_index('Unnamed: 0', inplace=True)

print(df.head())

player_height = df.loc[0:11145, ["player_height"]]

player_weight =df.loc[0:11145, ["player_weight"]]


#plt.scatter()
plt.title('Nba, peso e altura')
plt.xlabel(u'Peso')
plt.ylabel(u'Altura')
# #plt.oi()
# #plt.plot((1,2,3,4),(1,4,9,16), 'mD:')
plt.plot(player_weight, player_height, color='purple')
#plt.axis((0,6,0,20))



plt.show()


