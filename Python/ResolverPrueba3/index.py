
import funciones as fn 

print("Bienvenido al cafe PGY")

while True:
    print("-------------------------------------")
    print("Opción 1 - registro de cliente")
    print("Opción 2 - reserva de mesas")
    print("Opción 3 - Mostrar mesas")
    print("Opción 4 - Salir")
    print("-------------------------------------")
    
    option = int(input("Ingrese la opcion: "))
    if option == 1:
        while True:
            while True:
                nombre = input("Nombre: ")
                if fn.flag_nombre(nombre) == True:
                    break
                else:
                    print("Nombre invalido")
                    eleccion = input("Desea volver a intentarlo? (s/n): ")
                    if eleccion == "s":
                        continue
                    elif eleccion == "n":
                        break
            while True:
                correo = input("Correo: ")
                if fn.flag_correo(correo) == True:
                    break
                else:
                    print("correo invalido")
                    eleccion = input("Desea volver a intentarlo? (s/n): ")
                    if eleccion == "s":
                        continue
                    elif eleccion == "n":
                        break
            while True:
                celular = input("celular: ")
                if fn.flag_celular(celular) == True:
                    break
                else:
                    print("celular invalido")
                    eleccion = input("Desea volver a intentarlo? (s/n): ")
                    if eleccion == "s":
                        continue
                    elif eleccion == "n":
                        break
            break
    elif option == 2:
        correo = input("Porfavor ingrese un correo: ")
        try:
            mesa = fn.reserva(correo)
            print(f"Se ha registrado en la {mesa}")
            
        except:
            print("Correo no encontrado")
            
    elif option == 3:
        fn.datos_disponibles()
        print("-------------------------------------")
        fn.mesas_disponibles()
        
    elif option == 4:
        print("Gracias por usar nuestro servicio")
        break