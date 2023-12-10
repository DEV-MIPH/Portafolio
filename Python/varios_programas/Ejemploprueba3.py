
lista_nombre = []
lista_rut = []
lista_sexo = []
lista_ps = []
lista_correo = []
lista_edad = []
lista_hora = []
lista_comentario = []

print("Centro Médico DUOC")
while True:
    print("--------------------------------")
    try:
        print("1.	Registrar Paciente ")
        print("2.	Atención Paciente") 
        print("3.	Consultar Datos Paciente ")
        print("4.	Salir")
        

        option = int(input("Ingrese la opcion: "))
        print("--------------------------------")
        if option == 1:
            
            ps = ""
            
            nombre = input("Ingrese su nombre: ")
            lista_nombre.append(nombre)
            while True :
                try:
                    rut = int(input("Ingrese rut, sin dígito verificador ni puntos:  "))
                    if rut >= 5000000 and rut <= 99999999:
                        lista_rut.append(rut)
                        break
                except:
                    print("rut invalido")
            while True:
                try:
                    edad = int(input("Ingrese su edad: "))
                    if edad >= 0 and edad <= 110:
                        lista_edad.append(edad)
                        break
                except:
                    print("Edad invalida intente nuevamente")
            while True:
                try:
                    sexo = input("Ingrese su sexo (f o m): ")
                    sexo = sexo.lower()
                    if sexo == "f" or sexo == "m":
                        lista_sexo.append(sexo)
                        break
                except:
                    print("Seleccione una opcion valida (f o M)")
            while True:
                try:
                    ps = input("Ingrese su ps (ISAPRE o FONASA): ")
                    if ps == "ISAPRE" or ps == "FONASA":
                        lista_ps.append(ps)
                        break
                except:
                    print("Ingrese una opcion valida")
            key_correo = False
            while True:
                try:
                    correo = input("Ingrese su correo: ")
                    for i in correo:
                        if i == "@":
                            key_correo = True
                    if key_correo == True:
                        lista_correo.append(correo)
                        break
                except:
                    print("Correo invalido")
            
            
        if option == 2:
            try :
                
                rut_atencion = int(input("Ingrese el rut a atender: "))
            
                busqueda_atencion = lista_rut.index(rut_atencion)
                fecha_atencion = input("Ingrese su fecha de atencion ej: 20/01/2000: ")
                lista_hora.insert(busqueda_atencion, fecha_atencion)
                comentario = input("Ingrese su comentario:")
                lista_comentario.insert(busqueda_atencion, comentario)
                
            except:
                print("Rut invalido")
            
            
                
        if option == 3: 
            try:
                rut_consulta = int(input("Ingrese el rut a consultar: "))
                
                busqueda_consulta = lista_rut.index(rut_consulta)
                
                print(f"Nombre : \t\t{lista_nombre[busqueda_consulta]}")
                print(f"rut : \t\t\t{lista_rut[busqueda_consulta]}")
                print(f"edad : \t\t\t{lista_edad[busqueda_consulta]}")
                print(f"ps : \t\t\t{lista_ps[busqueda_consulta]}")
                print(f"correo : \t\t{lista_correo[busqueda_consulta]}")
                print(f"Fecha consulta : \t{lista_hora[busqueda_consulta]}")
                print(f"Comentario : \t\t{lista_comentario[busqueda_consulta]}")
            except:
                print("Rut no encontrado")
            
                
        if option == 4:
            try:
                salir = int(input("Seguro que desea salir 1.Si 2.No: "))
                if salir == 1:
                    print("Gracias por elegir el codigo IAGG")
                    print("Salir del sistema....")
                    break
            except:
                print("Seleccione opcion valida")
    except:
        print("Elija opcion valida...")
