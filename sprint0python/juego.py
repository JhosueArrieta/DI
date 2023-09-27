import random
lista = ["piedra","papel", "tijera"]
jugadas = 1
contg = 0
contp=0
conte=0
while (jugadas <= 5):
   
    def seleccionarAleatorio (lista):
        return random.choice (lista)
    guardo = seleccionarAleatorio(lista)
    print(guardo)
    opcion = (input (" Que deseas sacar (piedra/papel/tijera) ?"))
    while (opcion != "piedra") and (opcion != "papel") and (opcion != "tijera"):
        opcion = input ("Introduzca uno de los movimientos permitidos")
        
    if opcion==guardo : 
        print ("Has empatado")
        conte = conte + 1
        jugadas = jugadas + 1
    elif opcion == "papel" and guardo == "tijera":
        print ("Has perdido")
        contp = contp + 1
        jugadas = jugadas + 1
    elif opcion == "papel" and guardo == "piedra":
        print ("Has ganado ")
        contg = contg + 1
        jugadas = jugadas + 1

    elif opcion == "piedra" and guardo == "papel":
        print ("Has perdido")
        contp = contp + 1
        jugadas = jugadas + 1
    elif opcion == "piedra" and guardo == "tijera":
        print ("Has ganado ")
        contg = contg + 1
        jugadas = jugadas + 1

    elif opcion == "tijera" and guardo == "piedra":
        print ("Has perdido")
        contp = contp + 1
        jugadas = jugadas + 1
    elif opcion == "tijera" and guardo == "papel":
        print ("Has ganado ")
        contg = contg + 1
        jugadas = jugadas + 1
    

if contg > contp:
    print("Has ganado la partida")
elif contg < contp:
    print("Has perdido la partida")
elif conte == 5:
    print("Has empatado la partida")
elif conte > contp and conte > contg :
    print ("Partida nula")
        
    

    
    
        

