
import re


def factorial(numero):
    if numero == 1:#Hasta este valor se va a efectuar el bucle 
        return 1 
    else:
        return numero * factorial(numero-1)
        #Mientras el valor de numero != 1 se va a efectuar el bucle
   
numero = int(input('Numero: '))
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')