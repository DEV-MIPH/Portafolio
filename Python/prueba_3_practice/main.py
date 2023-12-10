
import funciones as fn

while True:
    print("Elija una de las siguientes opciones:")
    print("1) Registrar producto")
    print("2) Ver producto")
    print("3) Comprar producto")
    print("4) Salir")
    option = int(input("Opcion: "))
    
    if option == 1:
        while True:
            codigo = input("Ingrese el codigo: ")
            vali_codigo = fn.codigo_producto(codigo)
            if vali_codigo == True:
                break
        while True:
            nombre = input("Nombre: ")
            vali_nombre = fn.nombre_producto(nombre)
            if vali_nombre == True:
                break
        while True:
            precio = int(input("Precio: "))
            vali_precio = fn.precio_producto(precio)
            if vali_precio == True:
                break
        medida = input("Medida(K o U): ")
        medida = medida.upper()
        vali_medida = fn.medida_producto(medida)
        
    elif option == 2:
        codigo = input("Inserte el codigo del producto que desea buscar: ")
        fn.mostrar_producto(codigo)
        
    elif option == 3:
        fn.compra()
            
    
    elif option == 4:
        print("Adios")
        break 
    
    
    
        






