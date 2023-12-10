
import numpy as np

matriz = np.zeros((10,4),dtype=int)
cont = 0

for i in range(10):
    for j in range(4):
        cont += 1
        matriz[i,j] = cont 
        
print(matriz)