
import numpy as np
cont = 0
"""
arreglo1 = np.zeros((10,4),dtype=int)
for i in range(10):
    for j in range(4):
        cont += 1
        arreglo1[i,j] = cont
"""

array_2 = np.full((10,4), "          ")

for i in range(10):
    for j in range(4):
        cont += 1
        if array_2 [i,j] == array_2 [i,0]:
            array_2 [i][j] = (f"A{cont}")
        elif array_2 [i,j] == array_2 [i,1]:
            array_2 [i][j] = (f"B{cont}")
        elif array_2 [i,j] == array_2 [i,2]:
            array_2 [i][j] = (f"C{cont}")
        elif array_2 [i,j]== array_2 [i,3]:
            array_2 [i][j] = (f"D{cont}")


"""
print(array_2 )
position = np.where(array_2 == "B2")
print(position )    
valor = array_2[position]
print(valor)
"""

print("Bienvenido al sistema de eleccion de asientos IAGG")
print("Para empezar debera elegir si desea comprar, cancelar, o tener la informacion de algun asiento")
while True:
    print("1) Reservar un asiento")
    print("2) Cancelar asiento")
    print("3) Estado asiento")
    print("4) Salir")
    option = int(input("Seleccione una opcion: "))
    
    if option == 4:
        option = int(input("Seguro que deseas salir? 1)Si / 2)No "))
        if option == 1:
            print ("Adios")
            break
    
    

