
def menuPrincipal():
    print("""_______Bienvenidos a la gestión de Campus_______
          1. Gestión de Coordinador
          2. Gestión de Trainer
          3. Gestión de Camper
          4. Gestión de reportes
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
          0. Salir
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCoordinador():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de Coordinador_______
          1. Registrar las notas iniciales de un camper
          2. Crear una ruta de aprendizaje
          3. Crear los modulos de las rutas y su horario
          4. Ingresar un trainer a un salon
          5. Ingresar al camper en una ruta
          6. Ingresar las notas finales del modulo
          0. Salir
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc

def menuRutas(): 
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de rutas_______
          Rutas:
            1) Fundamentos de programacion
            2) Programacion Web
            3) Programacion formal
            4) Bases de datos
            5) Backend""")
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuReportes():
    print("""_______Bienvenidos a la gestión de Campus_______
          _______Gestión de reportes_______
            1. Listar los **campers** que se encuentren en estado de inscrito.
            2. Listar los **campers** que aprobaron el examen inicial.
            3. Listar los entrenadores que se encuentran trabajando con **CampusLands**.
            4. Listar los **campers** que cuentan con bajo rendimiento.
            5. Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.
            6. Mostrar cuantos **campers** perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
            0. Salir
            """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc