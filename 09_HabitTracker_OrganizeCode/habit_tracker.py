# habittracker.py

# 1. Usa nombres de variables y funciones descriptivos
# Lista para almacenar los hábitos diarios
habitos_diarios = []

# 2. Modulariza tu código
def agregar_habito(nombre, objetivo_diario):
    """Agrega un nuevo hábito a la lista."""
    habito = {
        'nombre': nombre,
        'objetivo_diario': objetivo_diario,
        'progreso': 0
    }
    habitos_diarios.append(habito)

def actualizar_habito(nombre, progreso):
    """Actualiza el progreso de un hábito."""
    for habito in habitos_diarios:
        if habito['nombre'] == nombre:
            habito['progreso'] += progreso
            if habito['progreso'] > habito['objetivo_diario']:
                habito['progreso'] = habito['objetivo_diario']
            return f"Progreso actualizado: {habito['progreso']}/{habito['objetivo_diario']}"
    return "Hábito no encontrado."

def mostrar_resumen_diario():
    """Muestra un resumen del progreso de todos los hábitos."""
    for habito in habitos_diarios:
        print(f"Hábito: {habito['nombre']} - Progreso: {habito['progreso']}/{habito['objetivo_diario']}")

def menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    while True:
        print("\n1. Agregar hábito")
        print("2. Actualizar hábito")
        print("3. Mostrar resumen diario")
        print("4. Salir")
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == '1':
            nombre = input("Introduce el nombre del hábito: ")
            objetivo = int(input(f"Introduce el objetivo diario para {nombre} (p. ej., 10 minutos, 5 kilómetros): "))
            agregar_habito(nombre, objetivo)
        elif opcion == '2':
            nombre = input("Introduce el nombre del hábito a actualizar: ")
            progreso = int(input(f"¿Cuánto progreso has hecho en {nombre}?: "))
            print(actualizar_habito(nombre, progreso))
        elif opcion == '3':
            mostrar_resumen_diario()
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    menu()
