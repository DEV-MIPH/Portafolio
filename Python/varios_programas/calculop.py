cont = 1
numero = 5
calculo = numero
elevacion = int(input("Ingrese la elevacion: "))
while True:
    calculo = calculo * numero
    cont += 1
    if cont == elevacion:
        break
print(calculo)

elevacion = int(input("Ingrese la elevacion: "))
numero = int(input("Ingrese numero: "))
total  = numero
for i in range(elevacion - 1):
    i = numero
    total = i * total
print(total)


elevacion = int(input("Ingrese la elevacion: "))
numero = int(input("Ingrese numero: "))
total = numero ** elevacion
print(total)
