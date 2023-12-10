
#La flecha solo es una pista y es opcional
def sumar(a,b) -> int:
    return (a + b)

resultado = sumar(5,3)
print(f'resultado de la suma: {resultado}')

def sumar(a = 0, b = 0):
    return(a + b)

#Con valores Default
resultado = sumar()
print(f'resultado de la suma: {resultado}')
#Los valores sobreescriben..
print(f'resultado de la suma: {sumar(2,8)}')


