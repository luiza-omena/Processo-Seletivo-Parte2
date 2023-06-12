import csv
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")

groups_list = []

# Leitura das informações do arquivo .csv
with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        if row["Age Group"] not in groups_list:
            groups_list.append(row["Age Group"])

size = len(groups_list)
single_list = [0] * size
multiple_list = [0] * size
single_percentage = [0] * size
multiple_percentage = [0] * size

with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        position = groups_list.index(row["Age Group"])
        if row["Crash Type"] == 'Single':
            single_list[position] += 1
        else:
            multiple_list[position] += 1

total_single = sum(single_list)
total_multiple = sum(multiple_list)

blank = groups_list.index('')
groups_list[blank] = "Indeterminado"

# Análise da representatividade de cada faixa em cada tipo
for i in range(size):
    single_percentage[i] = (single_list[i]/total_single) * 100
    multiple_percentage[i] = (multiple_list[i]/total_multiple) * 100

print("Porcentagem de pessoas em relação ao tipo de acidente (Single):")

for i in range(size):
    print(f"faixa de idade ({groups_list[i]}):\n {single_percentage[i]:.2f}%")

print("Porcentagem de pessoas em relação ao tipo de acidente (Multiple):")

for i in range(size):
    print(f"faixa de idade ({groups_list[i]}):\n {multiple_percentage[i]:.2f}%")


# Gráfico das informações adquiridas
labels = groups_list
single_quantity = single_list
multiple_quantity = multiple_list


cores = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'purple']



fig, (single, multiple) = plt.subplots(1, 2, figsize=(10, 5))


single.pie(single_quantity, colors=cores, autopct=lambda pct: f'{pct:.2f}%')
single.set_title('''Representatividade dos grupos de idade 
em relação ao tipo de acidente 
(Single).''')


multiple.pie(multiple_quantity, colors = cores, autopct=lambda pct: f'{pct:.2f}%')
multiple.set_title('''Representatividade dos grupos de idade 
em relação ao tipo de acidente 
(Multiple).''')

multiple.legend(labels, title='Grupos de Idade', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
