


lista_codigo = []
lista_nombre = []
lista_precio = []
lista_medida = []




def codigo_producto(codigo): 
    if len(codigo) == 4:
        lista_codigo.append(codigo)
        return True
    else:
        return (print("El codifo tiene que tener 4 digitos"))
    
def nombre_producto(nombre):    
    if len(nombre) >=3:
        lista_nombre.append(nombre)
        return True
    else:
        return(print("El nombre tiene que tener minimo 3 caracteres"))
    
def precio_producto(precio): 
    if precio > 0:
        lista_precio.append(precio)
        return True
    else:
        return(print("El precio tiene que ser mayor a 0"))
def medida_producto(medida):
    if medida == "K" or medida == "U":
        lista_medida.append(medida)
        return True
    else:
        return(print("La medida tiene que ser U o K"))


def mostrar_producto(codigo):
    if codigo in lista_codigo:
        search = lista_codigo.index(codigo)
        print("-------------------------------")
        print(f"Codigo: {lista_codigo[search]}")
        print(f"Nombre: {lista_nombre[search]}")
        print(f"Precio: {lista_precio[search]}")
        print(f"Medida: {lista_medida[search]}")
        print("-------------------------------")
    else:
        print("-------------------------------")
        print("\tCodigo no encontrado")
        print("-------------------------------")
    
def compra(): 
    for i in (lista_codigo):
        print(lista_codigo[i])
        
    