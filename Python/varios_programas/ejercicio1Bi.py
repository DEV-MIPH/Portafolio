'''
Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementos aleatorios de números enteros del 0 al 100.
'''
import numpy as np
import random

print("Bienvenidos a Matrices XD")
matriz = np.diag([1,1,1]) #crear matriz 3x3 con diagonal con 1's
print(matriz)

#recorrer matriz
for i in range(3):
    for j in range(3):
        print(matriz[i][j])
        
#llenar con números aleatorios
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
        

print(matriz)
print("Chao Pescao")

acumulador = 0

for i in range(3):
    for j in range(3):
        acumulador = acumulador + matriz[i][j]

promedio = acumulador /9

print(f"Promedio : {promedio}")
print(f"Suma : {acumulador}")

suma = matriz.sum()
print(f"Suma : {suma}")

mayor = 100
menor = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] < mayor:
            mayor = matriz[i][j]
        if matriz[i][j] > menor:
            menor = matriz [i][j]
            
print(f"menor : {menor}")
print(f"Mayor: {mayor}")

for i in range(3):
    for j in range(3):
        if i == j:
            print(matriz[i][j])
