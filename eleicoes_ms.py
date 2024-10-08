import pandas as pd
import matplotlib.pyplot as plt

### Gráficos Campo Grande MS

candidatos_cg = [
    "Adriane Lopes",
    "Rose Modesto",
    "Beto Pereira",
    "Camila Jara",
    "Beto Figueiró",
    "Luso de Queiroz",
    "Ubirajara Martins"
]

votos_cg = [
    140913,
    131525,
    115516,
    41966,
    10885,
    3108,
    1067
]
explode=(0,0,0,0,0,0,0)

plt.figure(figsize=(15,10))
plt.rcParams.update({'font.size':10})
labels = candidatos_cg
plt.pie(votos_cg,labels=labels,explode=explode,autopct='%2f%%',shadow=True)
plt.title("Eleição Prefeito Campo Grande MS")
plt.grid(True)


plt.show()

plt.figure(figsize=(15,10))
plt.bar(candidatos_cg,votos_cg,color= "skyblue")
plt.title("Eleição Prefeito campo Grande MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  

plt.show()

### Vereadores MS

vereadores_ms = [
    "Marquinhos Trad",
    "Rafael Tavares",
    "Carlão",
    "Silvio Pitu",
    "Veterinário Francisco",
    "Fábio Rocha",
    "Professor Riverton",
    "Junior Coringa",
    "Dr Victor Rocha",
    "Professor Juari",
    "Flavio Cabo Almi",
    "Luiza Ribeiro",
    "André Salineiro",
    "Papy",
    "Ana Portela",
    "Neto Santos",
    "Maicon Nogueira",
    "Delei Pinheiro",
    "Wilson Lands",
    "Herculano Borges"
]

votos_vereadores_ms = [
    8567,8128,6912,6409,6371,
    6314,6271,6131,5355,
    5050,5003,4982,4782,
    4641,4577,4576,
    4236,4179,4148,4119
]

plt.figure(figsize=(15, 15))
plt.rcParams.update({'font.size': 10})
labels= vereadores_ms
plt.pie(votos_vereadores_ms,labels=labels,autopct='%.2f%%', shadow=True)
plt.title('Eleição Vereadores Campo Grande - MS')
plt.grid(True)

plt.show()

plt.figure(figsize=(15,10))
plt.bar(vereadores_ms,votos_vereadores_ms,color= "skyblue")
plt.title("Eleição Vereadores campo Grande MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  

plt.show()

### Gráficos Dourados 


candidatos_dourados = [
    "Marçal Filho",
    "Alan Guedes",
    "Tiago Botelho",
    "Bela Barros",
    "Racib Harb"
]

votos_dourados = [
    60418,
    34027,
    17845,
    5476,
    2455
]

plt.figure(figsize=(14,10))
plt.rcParams.update({'font.size':10})
labels = candidatos_dourados
plt.pie(votos_dourados,labels=labels,autopct='%2f%%',shadow=True)
plt.title("Eleição Prefeito Dourados MS")
plt.grid(True)


plt.show()

plt.figure(figsize=(15,10))
plt.bar(candidatos_dourados,votos_dourados,color= "skyblue")
plt.title("Eleição Prefeito Dourados-MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  

plt.show()

### Gráficos Ponta Porã

candidatos_pp = [
    "Eduardo Campos",
    "Pompilio Júnior",
    "Carlos Bernardo",
    "Álvaro Soares"
]

votos_pp = [
    26473,
    15195,
    8168,
    1314
]

plt.figure(figsize=(14,10))
plt.rcParams.update({'font.size':10})
labels = candidatos_pp
plt.pie(votos_pp,labels=labels,autopct='%2f%%',shadow=True)
plt.title("Eleição Prefeito Ponta Porã MS")
plt.grid(True)


plt.show()

plt.figure(figsize=(15,10))
plt.bar(candidatos_dourados,votos_dourados,color= "skyblue")
plt.title("Eleição Prefeito Ponta Porã-MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  

plt.show()

### Três Lagoas


candidatos_tl = [
    "Dr Cassiano Maia",
    "Dr Ruy Costa",
    "Professor Vitor"
]

votos_tl = [
    38076,
    16027,
    1392
]

plt.figure(figsize=(14,10))
plt.rcParams.update({'font.size':10})
labels = candidatos_pp
plt.pie(votos_pp,labels=labels,autopct='%2f%%',shadow=True)
plt.title("Eleição Prefeito Três Lagoas MS")
plt.grid(True)


plt.show()

plt.figure(figsize=(15,10))
plt.bar(candidatos_dourados,votos_dourados,color= "skyblue")
plt.title("Eleição Prefeito Três Lagoas-MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  

### Corumbá

candidatos_corumba = [
    "Dr. Gabriel",
    "Luiz Antonio Pardal",
    "André Campos",
    "Delcídio Amaral"
]

votos_corumba = [
    28394,
    10659,
    5944,
    5043
]

plt.figure(figsize=(14,10))
plt.rcParams.update({'font.size':10})
labels = candidatos_pp
plt.pie(votos_pp,labels=labels,autopct='%2f%%',shadow=True)
plt.title("Eleição Prefeito Corumbá MS")
plt.grid(True)


plt.show()

plt.figure(figsize=(15,10))
plt.bar(candidatos_dourados,votos_dourados,color= "skyblue")
plt.title("Eleição Prefeito Corumbá-MS \"Gráfico em Barras\"")
plt.xlabel("Candidatos")
plt.ylabel("Número de Votos")
plt.xticks(rotation=45)  
plt.grid(axis='y')  