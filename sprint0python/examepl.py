def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}

opcion = input("Selecciona una operación (suma, resta, multiplicacion, division): ")

if opcion in operaciones:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = operaciones[opcion](num1, num2)
    print("El resultado es:", resultado)
else:
    print("Operación inválida. Por favor, selecciona una operación válida.")