import random
##pongo como clave de opciones y respuestas la propia adivinanza para asi poder trabajar sin el problema 
##que me da con claves de 1: 2: 3: 
adivinanzas = [
    "Que tiene MESSI que no tiene CR7?",
    "Que tiene iago en la panza?",
    "Que buga tiene victo jose?"
]
opciones = {
    "Que tiene MESSI que no tiene CR7?": " a. 5 balones de oro \n b. Un mundial \n c. Humildad ",
    "Que tiene iago en la panza?": " a. Empanadillas \n b. Yogures \n c. El ombligo ",
    "Que buga tiene victo jose?": " a. Lamborghini \n b. Fiat Multipla \n c. Peugeot 206"
}
respuestas = {
    "Que tiene MESSI que no tiene CR7?": "b",
    "Que tiene iago en la panza?": "a",
    "Que buga tiene victo jose?": "c"
}

adivinanzas_aleatorias = random.sample(adivinanzas, 2)

for adivinanza in adivinanzas_aleatorias:
    opcion = opciones[adivinanza]
    respuesta_correcta = respuestas[adivinanza]

    print(adivinanza)
    print(opcion)

    respuesta = input("Ingrese la opción correcta (a, b o c): ")

    if respuesta == respuesta_correcta:
        print("Correcto, has acertado")
    else:
        print("Incorrecto, te has equivocado")










