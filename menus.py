
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
          0. Salir
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc
    
def menuTrainer():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Trainer_______
          1. Registrar trainer
          2. Ingresar trainer a una ruta
          0. Salir
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCoordinador():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Coordinador_______
          1. Registrar las notas de un camper
          2. Ingresar un trainer a un salon
          3. Ingresar al camper en una ruta
          0. Salir
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc

def menuRutas():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de rutas_______
          Rutas:
            1) Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
            2) Programación Web (HTML, CSS y Bootstrap).
            3) Programación formal (Java, JavaScript, C#).
            4) Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
            5) Backend (NetCore, Spring Boot, NodeJS y Express).""")
    opc = int(input("Ingrese la opción deseada: "))
    return opc
