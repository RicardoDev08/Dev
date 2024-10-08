import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_seasons.csv")
df1 = df.loc[0:11145,["player_height"]]
df2 = df.loc[0:11145,["player_weight"]]

plt
salarios_minimos = [
    151,  # 2000
    180,  # 2001
    200,  # 2002
    240,  # 2003
    260,  # 2004
    300,  # 2005
    350,  # 2006
    380,  # 2007
    415,  # 2008
    465,  # 2009
    510,  # 2010
    545,  # 2011
    622,  # 2012
    678,  # 2013
    724,  # 2014
    788,  # 2015
    880,  # 2016
    937,  # 2017
    954,  # 2018
    998,  # 2019
    1045, # 2020
    1100  # 2021
]

anos = [
    2000,2001,2002,2003,2004,
    2005,2006,2007,2008,2009,
    2010,2011,2012,2013,2014,
    2015,2016,2017,2018,2019,
    2020, 2021
]
 
plt.title("salarios")
a=(salarios_minimos)
b=(anos)

plt.plot(a,b,'r--o')
plt.show()