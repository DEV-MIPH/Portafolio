import random
import string 
import numpy as np


array = np.diag(['','','','',]) 
cont = 0
lista = []

for i in range(4):
    for j in range(4):
        array[i,j] = random.choice(string.ascii_letters.lower())
        if array[i][j] == "a" or array[i][j] == "e" or array[i][j] == "i" \
        or array[i][j] == "o" or array[i][j] == "u":
            letra_mini = array[i,j]
            lista.append(letra_mini)
            cont += 1
            
print (array)
print(f"Las vocales son: {lista}")
print(f"La cantidad de vocales es: {cont}")

    




