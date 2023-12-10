import numpy as np
import random
array = np.full((3, 3), 0)
lista = []
lista_1= []
for i in range(3):
    for j in range(3):
        array[i][j] = random.randint(1,100)
        lista_1.append(array[i][j])
        if i == j:
            lista.append(array[i][j])
print (array)
print(lista)
print(lista_1)
lista_1.sort()
print(lista_1)