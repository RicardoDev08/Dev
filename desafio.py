import pandas as pd
print(pd.__version__)
df= pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(df.head())
# z=(df.query('Age < 10 & Survived == 1').head())
# z.to_csv('exercicio1.csv',sep=';',index=False,encoding='utf-8-sig')
#############################################################################################
# a=(df.query('Sex == "female" & Survived == 1').head())
# a.to_csv('exercicio2.csv',sep=';',index=False,encoding='utf-8-sig')
# b=(df.query(' Age > 50 & Survived == 1').head())
# b.to_csv('exercicio3.csv',sep=';',index=False,encoding='utf-8-sig')
# homem=(df.query(' Sex == "male" & Survived == 1').head())
# homem.to_csv('exercicio4.csv',sep=';',index=False,encoding='utf-8-sig')
# kid=(df.query(' Age < 12 & Survived == 1 & Sex =="female"').head())
# kid.to_csv('exercicio5.csv',sep=';',index=False,encoding='utf-8-sig')
