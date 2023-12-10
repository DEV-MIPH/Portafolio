
import imp
from pickletools import markobject


import numpy as np

matriz_zero= np.zeros((3,3),dtype=int)
cont = 0

for i in range(3):
    for j in range(3):
        if i == j:
            cont = cont + 1
            matriz_zero[i,j] = cont
print(matriz_zero)
            