
def suma():
def resta():
    print("") 
    print("RESTA")
    print("")
    
    num1=float(input("Ingrese el primer digito: ")) 
    num2=float(input("Ingrese el segundo digito: "))
    
    resta=num1-num2
    
    print("La resta es igual a: ", resta)

def multiplicacion():
    print('cuantos numeros desea multiplicar')
    cantidad=int(input())
    multiplicacion=1
    while cantidad>=1:
        print('por favor ingrese el numero que desea multiplicar')
        numero=float(input())
        multiplicacion=numero*multiplicacion
        cantidad=cantidad-1
    print('la multiplicacion es:', multiplicacion
def division():
    print ('///DIVISION///')
    print (' ')
    dividendo=float(input('   INGRESE EL NUMERO DIVIDENDO : '))
    divisor=float(input('   INGRESE EL NUMERO DIVISOR : '))
    print (' ')
    if (divisor < 1):
        print ('//EL DIVISOR ES CERO, INGRESE UN DIVISOR MAYOR A 0')
        division()
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
