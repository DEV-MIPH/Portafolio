
def option_1():
    while True:
        option = int(input("ingrese un numero entre 1 y 15: "))
        if option > 0 and option < 16:
            calc = option%2
            if calc == 0:
                print("-----------------------------------------")
                print("\nSu numero es primo\n")
                break   
            else:
                print("-----------------------------------------")
                print("\nTu numero no es primo\n")
                break

def option_2():
    while True:
        option = int(input("ingrese un numero para calcular su factorial entre 3 y 10: "))
        if option > 2 and option < 11:
            fac = 1
            for i in range(1, option + 1):
                fac *= i
            print("-----------------------------------------")
            print(f"El resultado de {option}! = {fac}")
            break

def option_3():
    while True:
        option = input("Ingrese la palabra: ")
        palabra_invertida = ""
        for i in option:
            palabra_invertida = i + palabra_invertida
        print("-----------------------------------------")
        print(f"Tu palabra invertida es {palabra_invertida}")
        if palabra_invertida == option:
            print("Tu palabra es palindrome")
            break
        else:
            print("Tu palabra no es palindrome")
            break

while True:
    print("-----------------------------------------")
    print("Elija una de las siguientes opciones: ")
    print("1) Número Primo")
    print("2) Factorial")
    print("3) Palíndrome")
    print("4) Salir")

    option = int(input("Ingrese la opcion a elegir: "))
    if option  == 4:
        print("Adios")
        break
    elif option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()