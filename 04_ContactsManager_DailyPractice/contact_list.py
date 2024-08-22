import os

# Ruta del archivo donde se guardarán los contactos
archivo_contactos = "contactos.txt"

def agregar_contacto(nombre, telefono, email):
    with open(archivo_contactos, "a") as archivo:
        archivo.write(f"{nombre},{telefono},{email}\n")
    print("Contacto agregado con éxito.")

def ver_contactos():
    if os.path.exists(archivo_contactos):
        with open(archivo_contactos, "r") as archivo:
            contactos = archivo.readlines()
            if contactos:
                print("\nAgenda de Contactos:")
                for contacto in contactos:
                    nombre, telefono, email = contacto.strip().split(',')
                    print(f"Nombre: {nombre} | Teléfono: {telefono} | Email: {email}")
            else:
                print("No hay contactos guardados.")
    else:
        print("No hay contactos guardados.")

def editar_contacto(nombre):
    if os.path.exists(archivo_contactos):
        with open(archivo_contactos, "r") as archivo:
            contactos = archivo.readlines()

        with open(archivo_contactos, "w") as archivo:
            encontrado = False
            for contacto in contactos:
                n, telefono, email = contacto.strip().split(',')
                if n == nombre:
                    nuevo_telefono = input("Introduce el nuevo teléfono: ")
                    nuevo_email = input("Introduce el nuevo email: ")
                    archivo.write(f"{n},{nuevo_telefono},{nuevo_email}\n")
                    encontrado = True
                else:
                    archivo.write(contacto)
                    
            if encontrado:
                print("Contacto editado con éxito.")
            else:
                print("No se encontró un contacto con ese nombre.")
    else:
        print("No hay contactos guardados.")

def eliminar_contacto(nombre):
    if os.path.exists(archivo_contactos):
        with open(archivo_contactos, "r") as archivo:
            contactos = archivo.readlines()

        with open(archivo_contactos, "w") as archivo:
            encontrado = False
            for contacto in contactos:
                n, telefono, email = contacto.strip().split(',')
                if n != nombre:
                    archivo.write(contacto)
                else:
                    encontrado = True

            if encontrado:
                print("Contacto eliminado con éxito.")
            else:
                print("No se encontró un contacto con ese nombre.")
    else:
        print("No hay contactos guardados.")

def menu():
    while True:
        print("\n1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == '1':
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            email = input("Introduce el email del contacto: ")
            agregar_contacto(nombre, telefono, email)
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            nombre = input("Introduce el nombre del contacto que quieres editar: ")
            editar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Introduce el nombre del contacto que quieres eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
