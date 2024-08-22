def calcular_calorias(alimentos):
    total_calorias = 0
    for alimento in alimentos:
        calorias = alimentos[alimento]['calorias']
        cantidad = alimentos[alimento]['cantidad']
        total_calorias += calorias * cantidad
    return total_calorias

def main():
    print("Bienvenido a la Calculadora de Calorías")
    
    # Diccionario para almacenar alimentos y sus calorías por porción
    alimentos = {}

    while True:
        try:
            nombre_alimento = input("Introduce el nombre del alimento (o escribe 'salir' para terminar): ")
            if nombre_alimento.lower() == 'salir':
                break
            
            calorias_por_porcion = float(input(f"Introduce las calorías por porción de {nombre_alimento}: "))
            cantidad_porciones = float(input(f"Introduce la cantidad de porciones consumidas de {nombre_alimento}: "))
            
            # Guardar el alimento en el diccionario
            alimentos[nombre_alimento] = {
                'calorias': calorias_por_porcion,
                'cantidad': cantidad_porciones
            }
            
        except ValueError:
            print("Error: Asegúrate de ingresar números válidos para las calorías y la cantidad de porciones.")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    total_calorias = calcular_calorias(alimentos)
    print(f"\nTotal de calorías consumidas en el día: {total_calorias:.2f}")

if __name__ == '__main__':
    main()
