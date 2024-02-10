def salida():
     while True:
        respuesta = input("¿Estás seguro de que quieres salir? (s/n): ").lower().strip()
        if respuesta == 's':
            print("Saliendo del programa...")
            return True
        elif respuesta == 'n':
            print("Volviendo al menú principal.")
            return False
        else:
            print("Opción no válida. Por favor, ingresa 's' para salir o 'n' para continuar.")
