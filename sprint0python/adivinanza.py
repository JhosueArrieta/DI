opcion = " "
adivinanza = "Que tiene MESSI que no tiene CR7? \n a. 5 balones de oro \n b. Un mundial \n c. Humildad  ";
print (adivinanza)
opcion = input("Que opcion es correcta?")
while (opcion != 'a') & (opcion != 'b') & (opcion != 'c'):
    opcion=input("Elige entre a/b/c ")
if opcion == "a":
    print ("Incorrecto")
elif opcion == "b":
    print ("Correcto")
else :
    print ("Incorrecto")


