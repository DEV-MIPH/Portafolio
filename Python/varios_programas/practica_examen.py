
import numpy as np

array = np.full((5,2),"  ")
cont = 0
for i in range(5):
    for j in range(2):
        cont += 1
        array[i][j] = cont
print(array)

numero = input("Ingrese un numero: ")
lista = []
lista.append(numero)
busqueda = np.where(array == numero)
lista_array = []
lista_array.append(busqueda)
array[busqueda] = "X"
print(array)
cancelar = input("Ingrese un numero para cancelar: ")
numero_cancelado = lista.index(cancelar) 
print(numero_cancelado)
if cancelar in lista:
    cancelado = lista_array[numero_cancelado]
    print(cancelado)
    array[cancelado] = cancelar
print(array)
