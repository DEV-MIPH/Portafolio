
import funciones as fn


print("Bienvenido al programa de calculo de factorial , invertir numeros y listar nombre")

while True:
    try:
        print("-----------------------------------------------")
        print("1. Calcular factorial")
        print("2. Invertir numeros")
        print("3. listar nombres")
        print("4. Salir")
        print("-----------------------------------------------")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            numero = int(input("Ingrese un numero: "))
            resultado = fn.factorial(numero)
            print(f"resultado de {numero}! es {resultado}")
        elif option == 2:
            numero = int(input("Ingrese un numero: "))
            resultado = fn.invertir(numero)
            print(f"{numero} invertido es {resultado}")
            
        elif option == 3:
            cantidad = int(input("Ingrese la cantidad de nombres: "))
            resultado = fn.lista_nombres(cantidad)
            print(f"Lista de nombres: {resultado}")
        elif option == 4:
            print("Saliendo del programa")
            break
    except:
        print("Opcion no valida")
        
