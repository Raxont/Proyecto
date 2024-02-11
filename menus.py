
def menuPrincipal():
    print("""_______Bienvenidos a la gestión de Campus_______
          1. Gestión de Coordinador
          2. Gestión de Trainer
          3. Gestión de Camper
          0. Salir""")
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCamper():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Camper_______
          1. Registrar camper
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc
    
def menuTrainer():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Trainer_______
          1. Registrar trainer
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCoordinador(campus):
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Coordinador_______
          1. Registrar las notas de un camper
          2. Ingresar al camper en una ruta
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc

