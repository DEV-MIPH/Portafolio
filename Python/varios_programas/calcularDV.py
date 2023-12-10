
def sacarDV(rut):
    lista = [2, 3, 4, 5, 6, 7, 2, 3,4,5,6,7,8]
    total = 0
    lista_2 = []
    rut = rut[::-1]
    for i in rut:
        num = int(i)
        lista_2.append(num)
    for i in range(len(lista_2)):
        total += lista[i] * lista_2[i]
    total_2 = total 
    total = total / 11
    total = int(total)
    total = total * 11
    total = total_2 - total
    dv = 11 - total
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "K"
    return dv

def main():
    rut = input("Ingrese su rut: ")
    dv = sacarDV(rut)
    print(f"Tu dv verificador es {dv}")
    
main()