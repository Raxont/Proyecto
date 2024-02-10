
def menuPrincipal():
    print("""_______Bienvenidos a la gestión de eventos_______
          1. Gestión de eventos
          2. Gestión de participantes
          0. Salir""")
    opc = int(input("Ingrese la opción deseada: "))
    return opc


def menuParticipantes():
    print("""_______Bienvenidos a la gestión de eventos_______
          _______Gestión de participantes_______
          1. Registrar participantes
          2. Eliminar participante
          3. Mostrar participantes que no han cancelado
          4. Saber cuantos participantes no han cancelado
          0. Salir al menu principal""")
    opc = int(input("Ingrese la opción deseada: "))
    return opc


def menuEventos():
    print("""_______Bienvenidos a la gestión de eventos_______
          _______Gestión de eventos_______
          1. Registrar eventos
          2. Marcar evento finalizado
          3. Modificar evento
          4. Eliminar evento
          5. Mostrar eventos
          0. Salir al menu principal""")
    opc = int(input("Ingrese la opción deseada: "))    
    return opc

def confirmacion():
    validacion = input("Ingrese salir para salir o cualquier otra opción o valor para continuar: ")
    if(validacion.lower() == "salir"):
        return True
    else:
        return False