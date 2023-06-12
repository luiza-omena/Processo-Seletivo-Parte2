import csv
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")

lista_grupos = []

with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        if row["Age Group"] not in lista_grupos:
            lista_grupos.append(row["Age Group"])

tamanho = len(lista_grupos)
lista_single = [0] * tamanho
lista_multiple = [0] * tamanho
single_porcentagem = [0] * tamanho
multiple_porcentagem = [0] * tamanho

with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        posicao = lista_grupos.index(row["Age Group"])
        if row["Crash Type"] == 'Single':
            lista_single[posicao] += 1
        else:
            lista_multiple[posicao] += 1

qtd_single = sum(lista_single)
qtd_multiple = sum(lista_multiple)

indeterminacao = lista_grupos.index('')
lista_grupos[indeterminacao] = "Indeterminado"

for i in range(tamanho):
    single_porcentagem[i] = (lista_single[i]/qtd_single) * 100
    multiple_porcentagem[i] = (lista_multiple[i]/qtd_multiple) * 100

print("Porcentagem de pessoas em relação ao tipo de acidente (Single):")

for i in range(tamanho):
    print(f"faixa de idade ({lista_grupos[i]}):\n {single_porcentagem[i]:.2f}%")

print("Porcentagem de pessoas em relação ao tipo de acidente (Multiple):")

for i in range(tamanho):
    print(f"faixa de idade ({lista_grupos[i]}):\n {lista_multiple[i]:.2f}%")



labels = lista_grupos
quantidades_single = lista_single
quantidades_multiple = lista_multiple


cores = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'purple']



fig, (single, multiple) = plt.subplots(1, 2, figsize=(10, 5))


single.pie(quantidades_single, colors=cores, autopct=lambda pct: f'{pct:.2f}%')
single.set_title('''Representatividade dos grupos de idade 
em relação ao tipo de acidente 
(Single).''')


multiple.pie(quantidades_multiple, colors = cores, autopct=lambda pct: f'{pct:.2f}%')
multiple.set_title('''Representatividade dos grupos de idade 
em relação ao tipo de acidente 
(Multiple).''')

multiple.legend(labels, title='Grupos de Idade', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
