import csv
import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

male_sum = 0
male_count = 0
female_sum  = 0
female_count = 0

#Leitura das informações do arquivo .csv
with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        if row["Year"] == "2021":
            if row["Gender"] == "Male":
                male_sum += int(row["Age"])
                male_count += 1

            elif row["Gender"] == "Female":
                female_sum += int(row["Age"])
                female_count += 1

mediaMale = (male_sum / male_count)
mediaFemale = (female_sum / female_count)

print(f"""A média de idade das pessoas do gênero feminino que morreram em acidentes de trânsito 
na Austrália no ano de 2021, foi: {mediaFemale:.2f}""")

print(f"""A média de idade das pessoas do gênero masculino que morreram em acidentes de trânsito
na Austrália no ano de 2021, foi: {mediaMale:.2f}""")

#Gráfico das informações adquiridas
genders = ["Masculino", "Feminino"]
media = [mediaMale, mediaFemale]

plt.figure(figsize=(8, 8))

for i in range(len(genders)):
    plt.bar(genders[i], media[i])
    plt.text(genders[i], media[i], f'{media[i]:.2f}', ha='center', va='bottom')

plt.xlabel('Gênero')
plt.ylabel('Média de idade')
plt.title('''Média de idade das pessoas que morreram em acidentes de trânsito 
na Austrália no ano de 2021, em relação ao gênero''')
plt.show()