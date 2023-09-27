from operaciones import suma,resta,multiplicacion,division

repetir = True
otra = " "
opcion = " "
operaciones = {
    1: "suma",
    2: "resta",
    3: "multiplicacion",
    4: "division"
}
while(repetir==True):
    
    opcion = (input("Selecciona operación a realizar. (suma,resta,multiplicación,division)"))
    while (opcion != "suma") & (opcion != "resta") & (opcion != "multiplicación") & (opcion != "division"):
        opcion = input("Elige una de las 4 operaciones matemáticas básicas: ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == operaciones[1]:
        print (suma(num1,num2))
    elif opcion == operaciones [2]:
        print (resta(num1,num2))
    elif opcion == operaciones[3]:
        print (multiplicacion(num1,num2))
    else:
        print (division(num1,num2))

    otra=input("Desea realizar otra operación: ")

    num1=0
    num2=0

    if (otra == "n"):
        break