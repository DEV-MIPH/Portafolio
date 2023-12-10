
while True:
    try:
        numero = int(input("Ingrese un numero: "))
        if numero > 0 and numero < 101:
            break
        else:
            print(f"El numero {numero} no es valido (Tiene que ser mayor a 1 y menor a 100")
    except:
        print("Ingrese un numero valido")
par = numero % 2
if par == 0:
    par = "es par"
else:
    par = "es impar"
    
lista = []
cont = 1
for i in range(numero):
    primo = numero / cont
    cont += 1
    if primo % 2 == 0 or primo % 2 == 1:
        lista.append(i)
if len(lista) == 2:
    resultado = "primo"
else:
    resultado = "no es primo"
    
print(f"El numero {numero} {par} y {resultado}")