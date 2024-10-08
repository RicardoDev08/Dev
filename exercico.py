import pandas as pd
import matplotlib.pyplot as plt

a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=(0,4,8,10)
d=(1,3,6,9)
# plt.plot((1,2,3,4,5),(1,2,3,4,5),'r')
# r == tipo cor da linha, -- == tipo fromatação da linha, o == pontos ligados da linha
plt.plot(a,b,'r --o')
plt.plot(c,d,'m--*')

# plt.hist(a,b)
# plt.scatter(a,b,'r--o')#
#plt.bar(a,b) # grafico de barras
plt.grid(True)
plt.axis((0,10,0,15))
plt.ylabel(u'Eixo y')
plt.xlabel(u'Eixo x')
plt.title('Gráfico do Ricardinho')

#############################################################################################################################################################
a=(10,20,30)
explode=(0,1,0,0)
labels = ["HB20","GOL","FUSCA"]


############################# Gráfico em pizza ########################################
# explode=(0.1,0,0)
# labels=["pizza","coca-cola","lasanha"]
# plt.pie(a,explode=explode,labels=labels,autopct='%.2f%%', shadow=True)
# plt.title('comida')
# plt.grid(True)
 
 
 


plt.show()

# df = pd.read_csv("all_seasons.csv")
# df1 = df.loc[0:11145,["player_height"]]
# df2 = df.loc[0:11145,["player_weight"]]