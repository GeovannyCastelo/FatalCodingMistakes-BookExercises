def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

def calculadora():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Introduce el número de la operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == '1':
        print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {num1} * {num2} = {multiplica(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Opción no válida. Por favor, selecciona una operación válida.")

# Ejecutar la calculadora
calculadora()
