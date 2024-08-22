def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    try:
        print("Bienvenido a la aplicación de conversión de moneda.")
        monto = float(input("Introduce la cantidad de dinero que deseas convertir: "))
        tasa_cambio = float(input("Introduce la tasa de cambio actual (por ejemplo, 1.1 para USD a EUR): "))
        
        resultado = convertir_moneda(monto, tasa_cambio)
        
        print(f"{monto} en la moneda original es igual a {resultado:.2f} en la moneda destino.")
    
    except ValueError as e:
        print("Error: Asegúrate de ingresar números válidos para el monto y la tasa de cambio.")
        print(f"Detalles del error: {e}")
    
    except Exception as e:
        print("Ocurrió un error inesperado.")
        print(f"Detalles del error: {e}")

if __name__ == '__main__':
    main()