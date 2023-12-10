
import numpy as np 
import random


matriz = np.diag([1,1,1])
print(matriz)

for i in range(3):
    for j in range(3):
        print(matriz[i][j])
        
#llenar con numeros aleatoreos
for i in range(3):
    for j in range(3):
        (matriz[i][j]) = random.randint(0,100)
print(matriz)
print("Adios")
print("hola")



