def suma():
    print("*****ESTAMOS EN LA OPERACIÓN DE SUMA*****")
    print("")
    print("Ingrese la cantidad de números que desea sumar. Se informa que solo puede ingresar números de tipo enteros. ")
    numeros=int(input()) 
    i=0
    suma=0
    while i <numeros:
        print("Ingrese el número que desea sumar ")
        cuales=int(input())
        suma=suma+cuales
        i=i+1
    print("La suma de los: ", cuales, " números es igual a: ", suma)    
def resta():
def multiplicacion():    
def division():
def menu():
    print(" ")
    print("///////////////////////Bienvenido al programa de calculadora///////////////////////")
    print("1. Suma.")
    print("2. Resta.")
    print("3. Multiplicacion.")
    print("4. Division.")
    print("5. Cerrar programa.")
    print(" ")
    decision=int(input("Ingrese el numero de la opcion que desea: "))
    if decision==1:
        suma()
    elif decision==2:
        resta()
    elif decision==3:
        multiplicacion()
    elif decision==4:
        division()
    elif decision==5:
        decision2=input("¿Esta seguro que desea salir del programa?: ")
        if decision2=="SI" or decision2=="Si" or decision2=="si":
            quit()
        else:
            menu()