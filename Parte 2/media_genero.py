import csv
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")
somaMale = 0
contMale = 0
somaFemale = 0
contFemale = 0
with open("CrashData.csv", "r") as cd:
    reader = csv.DictReader(cd)
    for row in reader:
        if row["Year"] == "2021":
            if row["Gender"] == "Male":
                somaMale += int(row["Age"])
                contMale += 1

            elif row["Gender"] == "Female":
                somaFemale += int(row["Age"])
                contFemale += 1

mediaMale = (somaMale / contMale)
mediaFemale = (somaFemale / contFemale)

print(f"""A média de idade das pessoas do gênero feminino que morreram em acidentes de trânsito 
na Austrália no ano de 2021, foi: {mediaFemale:.2f}""")

print(f"""A média de idade das pessoas do gênero masculino que morreram em acidentes de trânsito
na Austrália no ano de 2021, foi: {mediaMale:.2f}""")


# Plotar o gráfico de barras
genders = ["Masculino", "Feminino"]
media = [mediaMale, mediaFemale]

plt.figure(figsize=(8, 8))  # Definir tamanho da figura

for i in range(len(genders)):
    plt.bar(genders[i], media[i])
    plt.text(genders[i], media[i], f'{media[i]:.2f}', ha='center', va='bottom')

plt.xlabel('Gênero')
plt.ylabel('Média de idade')
plt.title('''Média de idade das pessoas que morreram em acidentes de trânsito 
na Austrália no ano de 2021, em relação ao gênero''')
plt.show()