import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_seasons.csv")
df1 = df.loc[0:899,["player_height"]]
df2 = df.loc[0:899,["player_weight"]]
print(df.head(10))
altura=(df1)
peso=(df2)
plt.scatter(altura,peso)
plt.grid(True)
plt.ylabel(u'peso')
plt.xlabel(u'altura')
plt.title('NBA')
plt.show()