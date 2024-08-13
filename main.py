import matplotlib.pyplot as plt
import numpy as np

num_fatias = int(input("Quantas fatias do gráfico quer gerar? "))

labels = []
sizes = []

for i in range(num_fatias):
    label = input(f"Digite o rótulo para a fatia {i+1}: ")
    size = float(input(f"Digite o tamanho da fatia {i+1}: "))
    labels.append(label)
    sizes.append(size)

destacar = int(
    input(f"Qual fatia você quer destacar? (1 a {num_fatias}) ")) - 1

explode = [0] * num_fatias
explode[destacar] = 0.1

plt.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gráfico Personalizado')
plt.axis('equal')
plt.show()
