
import numpy as np

array = np.zeros((10),dtype = int)
cont = 0

for i in range(10):
    cont += 1
    array[i] = cont
    
print(array)
