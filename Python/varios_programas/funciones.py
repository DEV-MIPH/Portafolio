

def saludo():
    print("Bienvenidos a funciones en Python")
    
#no tiene argumentos (entradas) y tiene retorno (salida)
def sumar():
    a = 3
    b = 5
    total = a + b
    return total

#tiene argumentos (entradas) y sin retorno (salida)
def restar(valor1, valor2):
    total = valor1 - valor2
    print(total)
    
#tiene argumentos (entradas) y tiene retorno (salida)
def multiplicar(valor1, valor2):
    total = valor1 * valor2
    return total

#........otros.......
def resta(a,b):
    return a - b

def resta1(a=None,b=None):
    if a==None or b==None:
        print("None")
        return
    return a-b

def calculo(precio,descuento):
    return precio - (precio * descuento / 100)  


def saludo(nombre, mensaje='Holaaa buenas tardes'):
    print(mensaje,nombre)
    

nombre = input("Ingrese su nombre: ")
saludo(nombre)
a = int(input("ingresa el numero 1: "))
b = int(input("ingresa el numero 2: "))
print(resta(a,b))
print(resta1(a,b))