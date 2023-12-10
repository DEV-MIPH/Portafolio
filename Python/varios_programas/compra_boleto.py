
import numpy as np
import os

list_name = []
list_rut = []
list_fono = []
list_num = []
list_dv = []
list_buy = []

cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0

cont_a_2 = 0
cont_b_2 = 0
cont_c_2 = 0
cont_d_2 = 0

array = np.full((10,4), "          ")
for i in range(10):
    for j in range(4):
        if array[i,j] == array [i,0]:
            cont_a += 1
            array [i][j] = (f"A{cont_a}")
        elif array [i,j] == array[i,1]:
            cont_b += 1
            array [i][j] = (f"B{cont_b}")
        elif array [i,j] == array [i,2]:
            cont_c += 1
            array [i][j] = (f"C{cont_c}")
        elif array [i,j]== array [i,3]:
            cont_d += 1
            array [i][j] = (f"D{cont_d}")
            
array_2 = np.full((10,4), "          ")
for i in range(10):
    for j in range(4):
        if array_2[i,j] == array_2 [i,0]:
            cont_a_2 += 1
            array_2 [i][j] = (f"A{cont_a_2}")
        elif array_2 [i,j] == array_2[i,1]:
            cont_b_2 += 1
            array_2 [i][j] = (f"B{cont_b_2}")
        elif array_2 [i,j] == array_2 [i,2]:
            cont_c_2 += 1
            array_2 [i][j] = (f"C{cont_c_2}")
        elif array_2 [i,j]== array_2 [i,3]:
            cont_d_2 += 1
            array_2 [i][j] = (f"D{cont_d_2}")

            
def option_1():
    print()
    
    print("Tiene los siguientes asientos para elegir")
    print(array)
    
    while True:
        choise = input("Seleccione un asiento: ")
        choise = choise.upper()
        buy = np.where(array == choise)
        if choise in list_num :
            print("Este asiento ya fue elegido")
            option = int(input("Desea volver a intentarlo 1)Si / 2)No: "))
            if option == 1:
                print("Asientos disponibles:")
                print(array)
                
            elif option == 2:
                break
        elif choise not in array:
            print(f"El asiento {choise} no existe, seleccione una opcion valida")
            option = int(input("Desea volver a intentarlo 1)Si / 2)No: "))
            if option == 2:
                break
        else:
            os.system("cls")
            list_buy.append(buy)
            list_num.append(choise)
            array[buy] = "X"
            print(f"Ha reservado el asiento {choise}")
            name = input("Por favor ingrese su nombre: ")
            list_name.append(name)
            rut = input("Ingrese su rut sin dv: ")
            dv = input("Ingrese su dv:")
            list_dv.append(dv)
            list_rut.append(rut)
            fono = input("Ingrese su fono: ")
            list_fono.append(fono)
            os.system("cls")
            print("---------------------------------------------------")
            print(f"    Asiento {choise} reservado para el rut: {rut}-{dv}")
            print("---------------------------------------------------")
            break
            
def option_2():

    choise_to_cancel = input("Ingrese el asiento a cancelar: ")
    choise_to_cancel= choise_to_cancel.upper()
    search_cancel = list_num.index(choise_to_cancel)
    if choise_to_cancel in list_num:
        confirm = int(input("Esta seguro 1)Si / 2)No: "))
        if confirm == 1:
            list_num.remove(choise_to_cancel)
            search_again = np.where(array_2 == choise_to_cancel )
            array[search_again] = choise_to_cancel
            del list_name[search_cancel]
            del list_rut[search_cancel]
            del list_dv[search_cancel]
            del list_fono[search_cancel]
            os.system("cls")
            os.system("clear")
   


def option_3():
    
    try:
        
        option= int(input("Desea consultar 1)Rut / 2)Asiento: "))
        if option == 1:
            search_rut = input("Ingrese el rut: ")
            search = list_rut.index(search_rut)
            print(f"Nombre: {list_name[search]}")
            print(f"rut: {list_rut[search]}-{list_dv[search]}")
            print(f"fono: {list_fono[search]}")
            print(f"Asiento: {list_num[search]}")
            os.system("pause")
            os.system("cls")
            os.system("clear")
        elif option == 2:
            search_choise = input("Inserte asiento: ")
            search_choise= search_choise.upper()
            search = list_num.index(search_choise)
            print(f"Nombre: {list_name[search]}")
            print(f"rut: {list_rut[search]}-{list_dv[search]}")
            print(f"fono: {list_fono[search]}")
            print(f"Asiento: {list_num[search]}")
            os.system("pause")
            os.system("cls")
            os.system("clear")
            
    except:
        os.system("cls")
        print("Lo siento rut o asiento no encontrado")
        
      
os.system("cls")
os.system("clear")
print ("Bienvenido al sistema de eleccion de asientos IAGG")
print("Para empezar debera elegir si desea comprar, cancelar, o tener la informacion de algun asiento")

while True:
    try:
        print("Opciones disponibles")
        print("1) Reservar un asiento")
        print("2) Cancelar asiento")
        print("3) Consulta asiento")
        print("4) Ver asientos disponibles")
        print("5) Salir")
        option = int(input("Seleccione una opcion: "))
        
        if option == 1:
            os.system("cls")
            os.system("clear")
            option_1()
        elif option == 2:
            os.system("cls")
            os.system("clear")
            try:
                option_2()
            except:
                print("No se encontro el asiento a cancelar")
        elif option == 3:
            os.system("cls")
            os.system("clear")
            option_3()
        elif option == 4:
            os.system("cls")
            os.system("clear")
            print("Estos son los asientos disponibles")
            print (array)
            os.system("pause")
            os.system("cls")
            os.system("clear")
        elif option == 5:
            option = int(input("Seguro que deseas salir? 1)Si / 2)No: "))
            if option == 1:
                print("Gracias por ocupar la seleccion de asientos IAGG ")
                break
        elif option != 1 or option != 2 or option != 3 or option != 4 or option != 5:
            os.system("cls")
            print("Seleccione una opcion valida")
    
    except:
        os.system("cls")
        print("Seleccione una opcion valida")
    
    