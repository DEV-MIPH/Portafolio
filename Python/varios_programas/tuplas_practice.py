
#Frutas es una tupla y no es modificable
frutas = ("Naranja", "Platano", "Sandia")
for i in frutas:
    print(i, end=" ")
#Si queremos modificar tenemos que transformar a lista y despues devolver a tupla
listaFruta = list(frutas)
listaFruta[0] = "Manzana"
frutas = tuple(listaFruta)
print("\n",frutas)
#eliminar tupla
del frutas
print(frutas)