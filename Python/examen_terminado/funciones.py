
def factorial(numero):
    total = 1
    cont = 1
    for i in range(numero-1):
        cont += 1
        resultado = cont * total
        total = resultado
    return (total)

def invertir (numero):
    
    # Este ejercicio tiene 2 respuestas correctas la segunda es mas corta pero
    # la primera es la que pide la profesora
    
    mod_1 = numero%10
    multi_1 = mod_1 * 10
    division_1 = int(numero/10)
    division_2 = int(division_1/10)
    mod_2 = division_1%10
    sumamod = multi_1 + mod_2
    multi_2 = sumamod *10
    division_3 = int(division_2/10)
    mod_3 = division_2%10
    multi_2 += mod_3
    
    return (multi_2)
    
    
    '''
    total = 0
    while numero > 0:
        total = total * 10 + numero % 10
        numero = numero // 10
    return (total)
    '''
    
def lista_nombres(cantidad):
    lista = []
    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        lista.append(nombre)
    return (lista)
    
    