
import numpy as np
import random 

lista_correo = []
lista_nombre = []
lista_celular = []
lista_mesa = []

cont = 0
mesas = np.full((5,2), "        ")

for i in range(5):
    for j in range(2):
        cont += 1
        mesas[i,j] = f"Mesa {cont}"


def flag_correo(correo):
    for i in correo:
        if i == "@":
            lista_correo.append(correo)
            return True
            

def flag_nombre(nombre):
    if len(nombre) > 1:
        lista_nombre.append(nombre)
        return True

def flag_celular(celular):
    if len(celular) == 9:
        lista_celular.append(celular)
        return True
    
def reserva(correo):
    if correo in lista_correo:
        while True:
            mesa = random.randint(1, 10)
            Mesa = f"Mesa {mesa}"
            if Mesa not in lista_mesa:
                lista_mesa.append(Mesa)
                search = np.where(mesas == Mesa)
                mesas[search] = "Ocupado"
                break
        return Mesa
            
def mesas_disponibles():
    print(mesas)

def datos_disponibles():
    for i in lista_nombre:
        for j in lista_mesa:
            print(f"Nombre: {i} - {j}")



