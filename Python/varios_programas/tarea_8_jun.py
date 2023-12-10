import numpy as np

acum = 0

matriz = np.diag([0,0,0]) 


for i in range(3):
    for j in range(3):
        i = 0
        j = 0 
        matriz[i,j] = 1
        acum += 1
        i = 1
        j = 1
        matriz[i,j] = 2
        acum += 1
        i = 2
        j = 2
        matriz[i,j] = 3
        acum += 1
print("👊🤮")
print(matriz)
        
    