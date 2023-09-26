opcion = " "
contCorrectas  = 0
adivinanzas = {
    1: "Que tiene MESSI que no tiene CR7?",
    2: "Que tiene iago en la panza?",
    3: "Que buga tiene victo jose?"
} 
opciones = {
    1: " a. 5 balones de oro \n b. Un mundial \n c. Humildad ",
    2: " a. Empanadillas \n b. Yogures \n c. El ombligo ",
    3: " a. Lamborghini \n b. Fiat Multipla \n c. Peugeot 206"
}
respuestas = {
    1: "b",
    2: "a",
    3: "c"
}

print("\n\tPrimera adivinanza")

print (adivinanzas[1])
print (opciones[1])
opcion = input("Que opcion es correcta?")
while (opcion != 'a') & (opcion != 'b') & (opcion != 'c'):
    opcion=input("Elige entre a/b/c ")
if opcion == respuestas[1] :
    print ("Correcto, + 10 puntos")
    contCorrectas = contCorrectas + 10
else :
    print ("Incorrecto, - 5 puntos")
    contCorrectas = contCorrectas -5 

print ( "\n\tSegunda adivinanza")

print (adivinanzas[2])
print (opciones[2])
opcion = input("Que opcion es correcta?")
while (opcion != 'a') & (opcion != 'b') & (opcion != 'c'):
    opcion=input("Elige entre a/b/c ")
if opcion == respuestas[2] :
    print ("Correcto, + 10 puntos")
    contCorrectas = contCorrectas + 10
else :
    print ("Incorrecto, - 5 puntos")
    contCorrectas = contCorrectas -5 

print ( "\n\tTercera adivinanza")

print (adivinanzas[3])
print (opciones[3])
opcion = input("Que opcion es correcta?")
while (opcion != 'a') & (opcion != 'b') & (opcion != 'c'):
    opcion=input("Elige entre a/b/c ")
if opcion == respuestas[3] :
    print ("Correcto, + 10 puntos")
    contCorrectas = contCorrectas + 10
else :
    print ("Incorrecto, - 5 puntos")
    contCorrectas = contCorrectas -5 
##para concatenar strings con ints utilizamos str(variable numérica) como sql
##hacer en clase o casa git add * git commit.. y git push
print("Tu puntuación es : " + str(contCorrectas))









