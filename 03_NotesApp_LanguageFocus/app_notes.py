import os

# Ruta del archivo donde se guardarán las notas
archivo_notas = "notas.txt"

def agregar_nota(titulo, contenido):
    with open(archivo_notas, "a") as archivo:
        archivo.write(f"{titulo}\n{contenido}\n---\n")
    print("Nota agregada con éxito.")

def ver_notas():
    if os.path.exists(archivo_notas):
        with open(archivo_notas, "r") as archivo:
            print(archivo.read())
    else:
        print("No hay notas guardadas aún.")

def editar_nota(titulo):
    if os.path.exists(archivo_notas):
        with open(archivo_notas, "r") as archivo:
            lineas = archivo.readlines()

        with open(archivo_notas, "w") as archivo:
            encontrado = False
            for i in range(0, len(lineas), 3):
                if lineas[i].strip() == titulo:
                    nuevo_contenido = input("Introduce el nuevo contenido: ")
                    lineas[i+1] = nuevo_contenido + "\n"
                    encontrado = True
                archivo.write(lineas[i] + lineas[i+1] + lineas[i+2])

            if encontrado:
                print("Nota editada con éxito.")
            else:
                print("No se encontró una nota con ese título.")
    else:
        print("No hay notas guardadas aún.")

def eliminar_nota(titulo):
    if os.path.exists(archivo_notas):
        with open(archivo_notas, "r") as archivo:
            lineas = archivo.readlines()

        with open(archivo_notas, "w") as archivo:
            encontrado = False
            for i in range(0, len(lineas), 3):
                if lineas[i].strip() != titulo:
                    archivo.write(lineas[i] + lineas[i+1] + lineas[i+2])
                else:
                    encontrado = True

            if encontrado:
                print("Nota eliminada con éxito.")
            else:
                print("No se encontró una nota con ese título.")
    else:
        print("No hay notas guardadas aún.")

def menu():
    while True:
        print("\n1. Agregar nota")
        print("\n2. Ver notas")
        print("\n3. Editar nota")
        print("\n4. Eliminar nota")
        print("\n5. Salir")
        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == '1':
            titulo = input("Introduce el título de la nota: ")
            contenido = input("Introduce el contenido de la nota: ")
            agregar_nota(titulo, contenido)
        elif opcion == '2':
            ver_notas()
        elif opcion == '3':
            titulo = input("Introduce el título de la nota que quieres editar: ")
            editar_nota(titulo)
        elif opcion == '4':
            titulo = input("Introduce el título de la nota que quieres eliminar: ")
            eliminar_nota(titulo)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
