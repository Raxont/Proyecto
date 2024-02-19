<h1>Proyecto Python Camilo Andres Navas Medina</h1>

<p>Aquí esta la informacion sobre mi proyecto, junto con instrucciones de como usarlo y una descripcion de su contenido</p>
<h2>Requerimientos a cumplir: </h2>
<p>El programa de seguimiento académico para CampusLands permite registrar la información de los campers inscritos y trainers en su programa intensivo de programación. Además, gestiona las rutas de entrenamiento creando salones y modulos con su horario respectivo, asigna campers y trainers a los salones, registra notas, y genera reportes. Algunas características principales incluyen:</p>
<ul>
  <li>Registro de campers con información detallada.</li>
  <li>Gestión de rutas de entrenamiento para la creacion de salones y modulos.</li>
  <li>Roles de usuario para Camper, Trainer y Coordinador.</li>
  <li>Evaluación de campers con pruebas teóricas y prácticas.</li>
  <li>Identificación de campers en riesgo alto y bajo rendimiento.</li>
  <li>Reportes sobre campers, trainers y los salones.</li>
  <li>Da una solución completa para el seguimiento y gestión del proceso de formación en CampusLands para un uso simple.</li>
</ul>
<h2>Desarollo del proyecto:</h2>
<p></p>Elegí enforcarlo como una plataforma de gestión del coordinador, donde hay roles y cada uno tiene sus distintas funciones. Para poder darle este enfoque, fue necesario utilizar varios modulos y archivos .json, los cuales listaré a continuación.</p>
<h3>Modulos
<ul>
  <li>El archivo del codigo principal el cual es el "Main.py"</li>
  <li>Archivos .py</li>
    <ul>
      <li>academico.py</li>
      <li>confirmarsalida.py</li>
      <li>estudiante.py</li>
      <li>menus.py</li>
      <li>notas.py</li>
      <li>profesor.py</li>
      <li>reportes.py</li>
    </ul>
  <li>Archivos .json</li>
    <ul>
      <li>estudiantes.json</li>
      <li>profesor.json</li>
      <li>rutas.json</li>
    </ul>
</ul>
<p>- Estos ultimos son usados para tener permanencia de datos para no perderlos al cerrar el codigo e ir modificando a medida que se requiera</p>
<h2>Main.py</h2>
<p>Aca tenemos el codigo principal el cual usamos para que todo el programa funcione.</p>
import confirmarsalida
import estudiante
import academico
import menus
import profesor
import reportes
#Programa para llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
while True:
    try:
        opc = menus.menuPrincipal()
        if opc == 1:
            #Menu Coordinador------------------------------------------------------
            clave=input("Ingrese la clave del coordinador para ingresar: ")
            if clave=="1":
               opcCorrdinador=menus.menuCoordinador()
               academico.m(opcCorrdinador)
            else:
                print("Clave incorrecta")
        elif opc == 2:
            #Menu Trainer-----------------------------------------------------
            clave=input("Ingrese la clave del Trainer para ingresar: ")
            if clave=="2":
                opcp = menus.menuTrainer()
                profesor.menu(opcp)
            else:
                print("Clave incorrecta")
        elif opc==3:
            #Menu Camper-----------------------------------------------
            op=menus.menuCamper()
            estudiante.opcc(op)
        elif opc==4:
            #Menu reportes ----------------------------------------------
            opcior=menus.menuReportes()
            reportes.imp(opcior)
        elif opc == 0:
            #Salir
            if confirmarsalida.salida():
                break
        else:
            #Error para numeros-------------------------------------------
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        #Error para la opc--------------------------------------------------
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")
<h2>academico.py</h2>
<p>Es nuestro codigo donde entramos como el coordinador del Campusland y vamos realizando unas tareas especificas para el programa donde solo entramos a este si sabemos la clave de ingreso ya que es el que nos permite realizar la mayoria de eventos en el programa</p>
import menus
import confirmarsalida
import notas
import json
#Opciones del menu del coordinador --------------------------------------------------------
def m(opcion):
    try:
        if opcion==1: #Registrar notas iniciales del camper ------------------------------------------
            notas.notar()
        elif opcion==2: #Crear una ruta --------------------------------------------------------------
            verificar=0
            with open('rutas.json', 'r') as ruta_file:
                ruta_info = json.load(ruta_file)
            op=menus.menuRutas()
            if op==1:
                op="Fundamentos de programacion"
            elif op==2:
                op="Programacion Web"
            elif op==3:
                op="Programacion formal"
            elif op==4:
                op="Bases de datos"
            elif op==5:
                op="Backend"
            else:
                print("Opcion incorrecta")        
            for x in ruta_info:   
                if op in x["nombre"]:
                    verificar=verificar+1
            if verificar==0:   
                nueva_ruta = {
                "nombre":op,
                "salon":{
                            "1":{"trainer":[]},
                            "2":{"trainer":[]},
                            "3":{"trainer":[]}
                        }
                    }
                ruta_info.append(nueva_ruta)
                print("*************************************")
                print("*    Ruta agregada correctamente    *")
                print("*************************************")
                print("")
                print("Regresando al menu...")
                with open ('rutas.json','w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
            elif verificar>0:
                print("Ya existe una ruta con la nombre de la ruta a crear ") 
        elif opcion==3: #Crear los modulos de las rutas y su horario ------------------------------------------------
            try:
                with open('rutas.json', 'r') as ruta_file:
                    ruta_info = json.load(ruta_file)
                print("Ingrese la ruta a la cual va a agregar el modulo ")
                opct=menus.menuRutas()
                if opct==1:
                    opct="Fundamentos de programacion"
                elif opct==2:
                    opct="Programacion Web"
                elif opct==3:
                    opct="Programacion formal"
                elif opct==4:
                    opct="Bases de datos"
                elif opct==5:
                    opct="Backend"
                else:
                    print("Opcion incorrecta")
                for f in ruta_info:
                    if opct==f['nombre']:
                        pos=ruta_info.index(f)
                        salon=str(input("Ingrese el salon a cual va a ser asignado(1-3): "))
                        while salon not in["1","2","3"]:
                            salon=int(input("Error, ingrese de nuevo el salon del camper (1-3): "))
                        modulo=str(input("Ingrese el nombre del modulo: "))
                        if modulo in ruta_info:
                            print("Ya existe un modulo con el nombre del modulo a crear ")
                        else:    
                            tiempo=str(input("ingrese el horario del salon(dia,tarde,noche): ")).lower()
                            while tiempo!="dia" and tiempo!="tarde" and tiempo!="noche":
                                tiempo=str(input("Error, debe digitar una opcion indicada(dia,tarde,noche): ")).lower()
                            capacidad=int(input("Ingrese la capacidad del modulo: "))
                            nuevo_modulo={
                                "tiempo":tiempo,
                                "capacidad":capacidad,
                                modulo:{
                                "camper":[]
                                }
                            }
                            ruta_info[pos]["salon"][salon].update(nuevo_modulo)
                print("*************************************")
                print("*    Ruta agregada correctamente    *")
                print("*************************************")
                print("")
                print("Regresando al menu...")
                with open ('rutas.json','w') as ruta_file:
                        json.dump(ruta_info, ruta_file, indent=4)
            except Exception as e:
                print("*****************************")
                print("* Ingrese una opción válida *")
                print("*****************************")
        elif opcion==4: #Ingresar un trainer a un salon ---------------------------------
            with open('rutas.json', 'r') as ruta_file:
                ruta_info = json.load(ruta_file)
            with open('profesor.json', 'r') as profesor_file:
                profesor_info = json.load(profesor_file)
            bandera = str(input("Desea empezar a agregar profesores? (s/n): ")).lower()
            while bandera != "s" and bandera != "n":
                bandera = str(input("Error, indique si desea continuar agregando profesores? (s/n): ")).lower()
            while bandera == "s":
                agregar_profesor(profesor_info,ruta_info)
                with open('rutas.json', 'w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
                bandera = str(input("Desea continuar agragando profesores? (s/n): ")).lower()
                while bandera != "s" and bandera != "n":
                    bandera = str(input("Error, indique si desea continuar agregando campers? (s/n): ")).lower()
            print("Saliendo al menu...")
        elif opcion==5: #Asignar camper a una ruta -----------------------------------------
            with open('rutas.json', 'r') as ruta_file:
                ruta_info = json.load(ruta_file)
            with open('estudiantes.json', 'r') as estudiantes_file:
                estudiantes_info = json.load(estudiantes_file)
            bandera = str(input("Desea empezar a agregar estudiantes? (s/n): ")).lower()
            while bandera != "s" and bandera != "n":
                bandera = str(input("Error, indique si desea continuar agregando campers? (s/n): ")).lower()
            while bandera == "s":
                asignar_camper(estudiantes_info,ruta_info)
                with open('rutas.json', 'w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
                bandera = str(input("Desea continuar agragando estudiantes? (s/n): ")).lower()
                while bandera != "s" and bandera != "n":
                    bandera = str(input("Error, indique si desea continuar agregando campers? (s/n): ")).lower()
            print("Saliendo al menu...")
        elif opcion==6: #Registrar las notas del modulo ----------------------------------------------------------------
            notas.no()
        elif opcion==0: #Salir ---------------------------------------------------------------------
            print("********************************")
            print("Volviendo al menú principal.")
            print("********************************")
        else:
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")

def agregar_profesor(profesor_info,ruta_info):
    verificar=0
    encontrarnombre=1
    encontradoruta=1
    encontraropcion=1
    encontradoregistro=1
    try:    
        nombret=str(input("Ingrese el nombre del trainer: "))   
        for i in profesor_info:
            if i['nombre'] == nombret:
                print("Ingrese la ruta a la cual va a pertenecer el trainer ")
                opct=menus.menuRutas()
                if 1 <= opct <= 5:
                    opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
                    opct = opct_dict[opct]
                    for f in ruta_info:
                        if opct==f['nombre']:
                            pos=ruta_info.index(f)
                            salon=str(input("Ingrese el salon del trainer(1-3): "))
                            while salon not in ["1","2","3"]:
                                salon=str(input("Error, ingrese de nuevo el salon del trainer (1-3): "))
                            if i["tiempo"]==f["salon"][salon]["tiempo"]:    
                                for x in f["salon"][salon]["trainer"]:
                                    if nombret in x["nombre"]:
                                        verificar=verificar+1
                                if verificar==0:     
                                    ruta_info[pos]["salon"][salon]["trainer"].append(i)
                                    print("*************************************")
                                    print("* Estudiante agregada correctamente *")
                                    print("*************************************")
                                    print("\nRegresando al menu...")
                                    encontrarnombre=1
                                    encontradoruta=1
                                    encontraropcion=1
                                    encontradoregistro=1
                                    return False
                                else:
                                    encontradoregistro=0
                                    encontrarnombre=1
                                    encontradoruta=1
                                    encontraropcion=1
                                    print(f"El trainer {nombret} ya esta asignado a este modulo") 
                                    print("")
                                    return False
                            else:
                                print(f"El trainer {nombret} no puede ser asignado por la hora de la clase")
                                print("")
                                encontradoregistro=0
                                encontraropcion=1
                                encontrarnombre=1
                                encontradoruta=1
                                return False
                        else:
                            encontradoregistro=0
                            encontraropcion=0
                            encontrarnombre=1
                            encontradoruta=1
                else:
                    encontradoregistro=0
                    encontraropcion=0
                    encontrarnombre=1
                    encontradoruta=0
            else:
                encontradoregistro=0
                encontraropcion=0
                encontradoruta=0
                encontrarnombre=0
        if encontrarnombre==1:
            if encontraropcion==1:    
                if encontradoruta==1:
                    print("")
                elif encontradoruta==0:
                    print(f"La ruta {opct} no esta registrada.")
                    print("")
            elif encontraropcion==0:
                print("Opción incorrecta") 
                print("")
        elif encontrarnombre==0:    
            print(f"El trainer {nombret} no esta registrado.")
            print("")  
    except Exception as e:
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")
    
def asignar_camper(estudiantes_info, ruta_info):
    try:
        nombre=str(input("Ingrese el nombre del camper a asignar una ruta: "))
        bandera=False
        for estudiante in estudiantes_info:
            if estudiante['nombre'] == nombre:
                bandera=True
                print("Ingrese la ruta a la cual va a pertenecer el camper:")
                opct = menus.menuRutas()
                if 1 <= opct <= 5:
                    opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
                    opct_nombre = opct_dict[opct]
                    for i, ruta in enumerate(ruta_info):
                        if ruta['nombre']==opct_nombre:
                            salon = input("Ingrese el salon del camper (1-3): ")
                            while salon not in ["1", "2", "3"]:
                                salon = input("Error, ingrese de nuevo el salon del camper (1-3): ")
                            modulo = input("Ingrese el nombre del modulo a asignar: ")
                            if modulo in ruta["salon"][salon]:
                                if estudiante["inicial"] == "Aprobado" and len(ruta["salon"][salon][modulo]["camper"]) <= ruta["salon"][salon]["capacidad"]:
                                    if not any(f["nombre"] == nombre for f in ruta["salon"][salon][modulo]["camper"]):
                                        ruta_info[i]["salon"][salon][modulo]["camper"].append(estudiante)
                                        print("*************************************")
                                        print("* Estudiante agregada correctamente *")
                                        print("*************************************")
                                        print("\nRegresando al menu...")
                                    else:
                                        print(f"\nEl camper {nombre} ya esto asignado a este modulo.")
                                else:
                                    print(f"\n{nombre} no cumple con los requisitos para ser asignado a este modulo.")
                            else:
                                print(f"\nEl modulo {modulo} no esto registrado.")
                            break
                    else:
                        print(f"\nLa ruta {opct_nombre} no está registrada.")
                else:
                    print("\nOpcion incorrecta")
                break
        if not bandera:
            print(f"\nEl camper {nombre} no está registrado.")
    except Exception as e:
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")
<h2>confirmarsalida.py</h2>
<p>Es un codigo simple donde nos indica si en verdad deseamos salir del programa principal el cual es nuestro "Main.py" y asi cerrar el programa</p>
def salida():
     while True:
        respuesta = input("¿Estás seguro de que quieres salir? (s/n): ").lower().strip()
        if respuesta == 's':
            print("Saliendo...")
            return True
        elif respuesta == 'n':
            print("Volviendo al menú principal.")
            return False
        else:
            print("Opción no válida. Por favor, ingresa 's' para salir o 'n' para continuar.")
<h2>estudiante.py</h2>
<p>Es el codigo donde ingresamos los datos del estudiante y los guardamos en el archivo "estudiantes.json"</p>
import json
#Funcion para ingresar los datos de un camper ----------------------------------------
def regparticipantes():
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    d={
        "nombre":input("Ingrese el nombre del camper: "),
        "apellido":input("Ingrese el apellido del camper: "),
        "documento":input("Ingrese el # de documento del camper: "),
        "direccion":input("Ingrese la direccion del camper: "),
        "acudiente":input("Ingrese el nombre del acudiente del camper: "),
        "telefono":input("Ingrese el # de celular y # fijo del camper: "),
        "estado":"En proceso de ingreso",
        "inicial":"Aprobado",
        "rendimiento":"medio",
        "riesgo":"bajo",
        "atencion":"no"
    }
    estudiantes_info.append(d)
    print("*************************************")
    print("* Estudiante agregado correctamente *")
    print("*************************************")
    print("")
    print("Regresando al menu...")
    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4) 

#Opciones del menu del camper --------------------------------------------------------
def opcc(opcion):
    if opcion == 1:
        regparticipantes()
    elif opcion == 0: 
        #Salir
        print("********************************")
        print("Volviendo al menú principal.")
        print("********************************")
    else:
        print("************************************")
        print("* El valor no está en las opciones *")
        print("************************************")

<h2>menus.py</h2>
<p>Nos muestra segun las opciones escogidas en el "Main.py" unos menu donde solo nos funciona para recoger el valor de la opcion ingresada en este codigo e imprimir los menu de manera comprensible</p>

def menuPrincipal():
    print(""" 
              ____________________________________
             | Bienvenidos a la gestión de Campus |
             |____________________________________|
             |  1. Gestión de Coordinador         |
             |  2. Gestión de Trainer             |
             |  3. Gestión de Camper              |
             |  4. Gestión de reportes            | 
             |  0. Salir                          |
             |____________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCamper():
    print("""
              ____________________________________
             | Bienvenidos a la gestión de Campus |
             |____________________________________|
             |---------Gestión de Camper----------|
             | 1. Registrar camper                |
             | 0. Salir                           | 
             |____________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc
    
def menuTrainer():
    print("""
              ____________________________________
             | Bienvenidos a la gestión de Campus |
             |____________________________________|
             |---------Gestión de Trainer---------|
             | 1. Registrar trainer               |
             | 0. Salir                           | 
             |____________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuCoordinador():
    print("""
              _________________________________________________
             |        Bienvenidos a la gestión de Campus       |
             |_________________________________________________|
             |---------------Gestion de Coordinador------------|
             | 1. Registrar las notas iniciales de un camper   |
             | 2. Crear una ruta de aprendizaje                |
             | 3. Crear los modulos de las rutas y su horario  |
             | 4. Ingresar un trainer a un salon               |   
             | 5. Ingresar al camper en una ruta               | 
             | 6. Ingresar las notas finales del modulo        |
             | 0. Salir                                        |
             |_________________________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))    
    return opc

def menuRutas(): 
    print("""
              ____________________________________
             | Bienvenidos a la gestión de Campus |
             |____________________________________|
             |-------------Rutas------------------|
             | 1. Fundamentos de programacion     |
             | 2. Programacion Web                |
             | 3. Programacion formal             |
             | 4. Bases de datos                  |   
             | 5. Backend                         | 
             |____________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menuReportes():
    print("""
              __________________________________________________________________________
             |                  Bienvenidos a la gestión de Campus                      |
             |__________________________________________________________________________|
             |---------------------------Gestion de Reportes----------------------------|
             | 1. Listar los campers que se encuentren en estado de inscrito            |
             | 2. Listar los campers que aprobaron el examen inicial                    |
             | 3. Listar los entrenadores que se encuentran trabajando con CampusLands  |
             | 4. Listar los campers que cuentan con bajo rendimiento                   |   
             | 5. Listar los campers y trainers que se encuentren asociados a una ruta  |     
             | 6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos |
             | 0. Salir                                                                 |
             |__________________________________________________________________________|
          """)
    opc = int(input("Ingrese la opción deseada: "))
    return opc
<h2>notas.py</h2>
<p>Nos sirve para registrar las notas del estudiante sea la nota del examen inicial o las notas del examen final de cada modulo</p>
import json
import menus
def no(): #Notas finales.......................................................................
    try:
        with open('rutas.json', 'r') as ruta_file:
            ruta_info = json.load(ruta_file)
        with open('estudiantes.json', 'r') as estudiantes_file:
            estudiantes_info = json.load(estudiantes_file)
        nombre=str(input("Ingrese el nombre del camper: "))
        bandera=False
        for estudiante in estudiantes_info:
            if estudiante['nombre'] == nombre:
                bandera=True
                print("Ingrese la ruta a la cual pertenece el camper:")
                opct = menus.menuRutas()
                if 1 <= opct <= 5:
                    opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
                    opct_nombre = opct_dict[opct]
                    for i, ruta in enumerate(ruta_info):
                        if ruta['nombre']==opct_nombre:
                            salon = input("Ingrese el salon del camper (1-3): ")
                            while salon not in ["1", "2", "3"]:
                                salon = input("Error, ingrese de nuevo el salon del camper (1-3): ")
                            modulo = input("Ingrese el nombre del modulo que pertenece el camper: ")
                            if modulo in ruta["salon"][salon]: 
                                for f in ruta["salon"][salon][modulo]["camper"]:
                                    if f["nombre"]==nombre:
                                        teorica=float(input("Ingrese la nota teorica: "))
                                        practica=float(input("Ingrese la nota practica: "))
                                        trabajo=float(input("Ingrese la nota de los trabajos y quizes: "))
                                        total=(teorica*0.3)+(practica*0.6)+(trabajo*0.1)
                                        if total>=60:
                                            f["final"]="Cursando"
                                            if total>=60 and total<70: 
                                                f["rendimiento"]="bajo"
                                                f["riesgo"]="alto"
                                                f["atencion"]="si"
                                            elif total>=70 and total<90:
                                                f["rendimiento"]="medio"
                                                f["riesgo"]="medio"
                                                f["atencion"]="no"
                                            elif total>=90:
                                                f["rendimiento"]="alto"
                                                f["riesgo"]="bajo"
                                                f["atencion"]="no"
                                        else:
                                            f["final"]="Expulsado"
                                            f["rendimiento"]="bajo"
                                            f["riesgo"]="alto"
                                            f["atencion"]="si"
                                        f["NotaFinal"]=total 
                                        print("***********************************")
                                        print("* Notas registradas correctamente *")
                                        print("***********************************")
                                        print("\nRegresando al menu...")
                                        break
                                else:
                                    print(f"\nEl camper {nombre} no se encontró registrado en el modulo.")
                            else:
                                print(f"\nEl modulo {modulo} no esto registrado.")
                            break
                    else:
                        print(f"\nLa ruta {opct_nombre} no está registrada.")
                else:
                    print("\nOpcion incorrecta")
                break
        if not bandera:
            print(f"\nEl camper {nombre} no está registrado en la base de datos.")
        with open('rutas.json', 'w') as ruta_file:
            json.dump(ruta_info, ruta_file, indent=4)
    except Exception as e:
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")

            
def notar(): #Notas iniciales..................................................................................
    encontradonombre=1
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    for i in estudiantes_info:
        if i["nombre"]==nombre:
            teorica=float(input("Ingrese la nota teorica: "))
            practica=float(input("Ingrese la nota practica: "))
            total=(teorica+practica)/2
            if total>=60:
                i["inicial"]="Aprobado"
                i["estado"]="inscrito"
                if total>=60 and total<=70:  
                    i["rendimiento"]="bajo"
                    i["riesgo"]="alto"
                    i["atencion"]="si"
                elif total<70 and total<90:
                    i["rendimiento"]="medio"
                    i["riesgo"]="medio"
                    i["atencion"]="no"
                elif total>=90:
                    i["rendimiento"]="alto"
                    i["riesgo"]="bajo"
                    i["atencion"]="no"
            else:
                i["estado"]="Expulsado"
                i["inicial"]="No aprobado"
                i["riesgo"]="alto"
                i["atencion"]="si"
            encontradonombre=1
            i["NotaFinal"]=total
            print("***********************************")
            print("* Notas registradas correctamente *")
            print("***********************************")
            print("\nRegresando al menu...")
        else:
            encontradonombre=0    
    if encontradonombre==1:
        print("")
    elif encontradonombre==0:
        print(f"El camper {nombre} no se encontró registrado.")
        print("Volviendo al menu...")

    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4)
<h2>profesor.py</h2>
<p>Es el codigo donde ingresamos los datos del trainer y los guardamos en el archivo "profesor.json" </p>
import menus
import json
import confirmarsalida
#Funcion para ingresar los datos de un trainer ----------------------------------------
def regtrainer():
    with open('profesor.json', 'r') as profe_file:
        profe_info = json.load(profe_file)
    nombre=str(input("Ingrese el nombre del trainer: "))
    apellido=str(input("Ingrese el apellido del trainer: "))
    tiempo=str(input("ingrese el horario del profesor(dia,tarde,noche): ")).lower()
    while tiempo!="dia" and tiempo!="tarde" and tiempo!="noche":
        tiempo=str(input("Error, debe digitar una opcion indicada(dia,tarde,noche): ")).lower()
    d={
        "nombre":nombre,
        "apellido":apellido,
        "tiempo":tiempo
    }
    profe_info.append(d)
    print("*************************************")
    print("* Profesor agregado correctamente *")
    print("*************************************")
    print("")
    print("Regresando al menu...")
    with open ('profesor.json','w') as profe_file:
        json.dump(profe_info, profe_file, indent=4) 

#Opciones del menu del trainer --------------------------------------------------------
def menu(opcion):
    try:    
        if opcion == 1:
            regtrainer()
        elif opcion == 0:
            print("********************************")
            print("Volviendo al menú principal.")
            print("********************************")
        else: 
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except:
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")
<h2>reportes.py</h2>
<p>Es el codigo que usamos para realizar la impresion final dependiendo de la opcion que desea del usuario, usando la informacion guardada en los 3 archivos .json</p>
import json
import menus
def inscritos(): #Listar los campers que se encuentren en estado de inscrito-------------------------------------------------------
    contador=0
    verificar=1
    contadorp=1
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    try:
        while verificar<=len(estudiantes_info):
            for x in estudiantes_info:
                contador=contador+1
                if x["estado"]=="inscrito":
                    print(f"Los datos del estudiante #{contadorp} inscrito son:")
                    for key,val in x.items():
                        print(f"{key} = {val}")
                    verificar=verificar+1
                    bander=input("Desea mostrar la informacion de otro camper?(s/n): ").lower()
                    while bander!="s" and bander!="n":
                        bander=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
                    if bander=="s":
                        contadorp=contadorp+1
                        print("Mostrando otro camper...")
                        print("")
                    elif bander=="n":
                        print("Saliendo al menu...")
                        print("")
                        return False
                else:
                    verificar=verificar+1
            if verificar>len(estudiantes_info):
                print("************************************")
                print("* No hay mas estudiantes inscritos *")
                print("************************************")
        if contador==0:
            print("No hay estudiantes registrados")
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
def aprobaron(): #Listar los campers que aprobaron el examen inicial..............................................
    contador=0
    verificar=1
    contadorp=1
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    try:
        while verificar<=len(estudiantes_info):
            for x in estudiantes_info:
                contador=contador+1
                if x["inicial"]=="Aprobado":
                    print(f"Los datos del estudiante #{contadorp} que aprobo el examen inicial son:")
                    for key,val in x.items():
                        print(f"{key} = {val}")
                    verificar=verificar+1
                    bander=input("Desea mostrar la informacion de otro camper?(s/n): ").lower()
                    while bander!="s" and bander!="n":
                        bander=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
                    if bander=="s":
                        contadorp=contadorp+1
                        print("Mostrando otro camper...")
                        print("")
                    elif bander=="n":
                        print("Saliendo al menu...")
                        print("")
                        return False
                else:
                    verificar=verificar+1
            if verificar>len(estudiantes_info):
                print("*********************************************************")
                print("* No hay mas estudiantes que aprobaron el primer examen *")
                print("*********************************************************")
                print("\nRegresando al menu...")
        if contador==0:
            print("No hay estudiantes registrados")
            print("\nRegresando al menu...")
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
        print("\nRegresando al menu...")
def trainers(): #Listar los entrenadores que se encuentran trabajando con CampusLands..........................................
    with open('profesor.json', 'r') as profe_file:
        profe_info = json.load(profe_file)
    contador=0
    verificar=1
    contadorp=1
    try:
        while verificar<=len(profe_info):
            for x in profe_info:
                contador=contador+1
                print(f"Los datos del profesor #{contadorp} que esta trabajando campusland son:")
                for key,val in x.items():
                    print(f"{key} = {val}")
                verificar=verificar+1
                bander=input("Desea mostrar la informacion de otro profesor?(s/n): ").lower()
                while bander!="s" and bander!="n":
                    bander=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
                if bander=="s":
                    contadorp=contadorp+1
                    print("Mostrando otro profesor...")
                    print("")
                elif bander=="n":
                    print("Saliendo al menu...")
                    print("")
                    return False
            if verificar>len(profe_info):
                print("************************************")
                print("* No hay mas profesores registrados *")
                print("************************************")
        if contador==0:
            print("No hay profesores registrados")
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
def rendimiento(): #Listar los campers que cuentan con bajo rendimiento.............................................
    contador=0
    verificar=1
    contadorp=1
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    try:
        while verificar<=len(estudiantes_info):
            for x in estudiantes_info:
                contador=contador+1
                if x["rendimiento"]=="bajo":
                    print(f"Los datos del estudiante #{contadorp} con bajo rendimiento son:")
                    for key,val in x.items():
                        print(f"{key} = {val}")
                    verificar=verificar+1
                    bander=input("Desea mostrar la informacion de otro camper?(s/n): ").lower()
                    while bander!="s" and bander!="n":
                        bander=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
                    if bander=="s":
                        contadorp=contadorp+1
                        print("Mostrando otro camper...")
                        print("")
                    elif bander=="n":
                        print("Saliendo al menu...")
                        print("")
                        return False
                else:
                    verificar=verificar+1
            if verificar>len(estudiantes_info):
                print("***********************************************")
                print("* No hay mas estudiantes con rendimiento bajo *")
                print("***********************************************")
                print("\nRegresando al menu...")
        if contador==0:
            print("No hay estudiantes registrados")
            print("\nRegresando al menu...")
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
        print("\nRegresando al menu...")
def asociados(): #Listar los campers y trainers que se encuentren asociados a una ruta-------------------------------------------------------
    with open('rutas.json', 'r') as ruta_file:
        ruta_info = json.load(ruta_file)
    verificar=1
    contador=0
    contadorp=1
    encontradomodulo=1
    encontradoruta=1
    encontradopcion=1
    try:
        print("Ingrese la ruta a la cual va a bucar el camper ")
        opct=menus.menuRutas()
        if 1 <= opct <= 5:
            opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
            opct = opct_dict[opct]
            for f in ruta_info:
                if opct == f['nombre']:
                    pos = ruta_info.index(f)
                    salon = str(input("Ingrese el salon del camper (1-3): "))
                    while salon not in ["1", "2", "3"]:
                        salon = str(input("Error, ingrese de nuevo el salon del camper (1-3): "))
                    print("Los datos del profesor del salon son:")
                    for y in f["salon"][salon]["trainer"]:
                        for key,val in y.items():
                            print(f"{key} = {val}")
                    print("")
                    modulo = str(input("Ingrese el nombre del modulo a buscar: "))
                    if modulo in f["salon"][salon]:
                        while verificar<=len(f["salon"][salon][modulo]["camper"]):
                            for x in f["salon"][salon][modulo]["camper"]:
                                print(f"Los datos del estudiante #{contadorp} inscrito son:")
                                for key,val in x.items():
                                    print(f"{key} = {val}")
                                verificar=verificar+1    
                                encontradomodulo=1
                                encontradoruta=1
                                encontradopcion=1
                                contador=1   
                                bander=input("Desea mostrar la informacion de otro camper?(s/n): ").lower()
                                while bander!="s" and bander!="n":
                                    bander=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
                                if bander=="s":
                                    print("Mostrando otro camper...")
                                    print("")
                                    contadorp=contadorp+1
                                elif bander=="n":
                                    print("Saliendo al menu...")
                                    print("")
                                    return False   
                        if verificar>len(f["salon"][salon][modulo]["camper"]):
                            print("*****************************************")
                            print("* No hay mas estudiantes en este modulo *")
                            print("*****************************************")    
                    else:
                        encontradomodulo=0
                        encontradoruta=1
                        encontradopcion=1
                else:
                    encontradomodulo=0
                    encontradoruta=0
                    encontradopcion=1
        else:
            encontradomodulo=0
            encontradoruta=0
            encontradopcion=0
        if encontradopcion==1:
            if encontradoruta==1:
                if encontradomodulo==1:
                    if contador==1:
                        print("")
                    elif contador==0:
                        print("No hay estudiantes inscritos en el modulo")
                elif encontradomodulo==0:
                    print(f"El modulo {modulo} no esta registrado.") 
            elif encontradoruta==0:
                print(f"La ruta {opct} no esta registrada.")          
        elif encontradopcion==0:    
            print("Opción incorrecta")          
    
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
def cantidad(): #Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos ....................................................
    with open('rutas.json', 'r') as ruta_file:
        ruta_info = json.load(ruta_file)
    contador=0
    cpasaron=0
    cperdieron=0
    encontradomodulo=1
    encontradoruta=1
    encontradopcion=1
    try:
        print("Ingrese la ruta a la cual va a bucar el camper ")
        opct=menus.menuRutas()
        if 1 <= opct <= 5:
            opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
            opct = opct_dict[opct]
            for f in ruta_info:
                if opct == f['nombre']:
                    pos = ruta_info.index(f)
                    salon = str(input("Ingrese el salon del camper (1-3): "))
                    while salon not in ["1", "2", "3"]:
                        salon = str(input("Error, ingrese de nuevo el salon del camper (1-3): "))
                    modulo = str(input("Ingrese el nombre del modulo a buscar: "))
                    if modulo in f["salon"][salon]:
                        for x in f["salon"][salon][modulo]["camper"]:                          
                            if x["final"]=="Cursando":
                                cpasaron=cpasaron+1
                            elif x["final"]=="Expulsado":
                                cperdieron=cperdieron+1   
                            encontradomodulo=1
                            encontradoruta=1
                            encontradopcion=1
                            contador=1      
                        print(f""" ________________________________________________________________
|   Cantidad de campers que aprobaron y no aprobaron el modulo   |
|________________________________________________________________|
  En el modulo {modulo}                                          
  El profesor encargado {f["salon"][salon]["trainer"][0]["nombre"]}        
  Cantidad de estudiantes que aprobaron: {cpasaron}              
  Cantidad de estudiantes que desaprobaron: {cperdieron}         
|________________________________________________________________|""")  
                        print("")
                        print("Regresando al menu...")
                    else:
                        encontradomodulo=0
                        encontradoruta=1
                        encontradopcion=1
                else:
                    encontradomodulo=0
                    encontradoruta=0
                    encontradopcion=1
        else:
            encontradomodulo=0
            encontradoruta=0
            encontradopcion=0
        if encontradopcion==1:
            if encontradoruta==1:
                if encontradomodulo==1:
                    if contador==1:
                        print("")
                    elif contador==0:
                        print("No hay estudiantes inscritos en el modulo")
                elif encontradomodulo==0:
                    print(f"El modulo {modulo} no esta registrado.") 
            elif encontradoruta==0:
                print(f"La ruta {opct} no esta registrada.")          
        elif encontradopcion==0:    
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")         
    except Exception as e:
        print("*****************************")
        print("*      Error desconocido    *")
        print("*****************************")
def imp(opcion): #Menu de los reportes
    try:
        if opcion==1: #Listar los campers que se encuentren en estado de inscrito.............................................
            inscritos() 
        elif opcion==2: #Listar los campers que aprobaron el examen inicial..............................................
            aprobaron()
        elif opcion==3: #Listar los entrenadores que se encuentran trabajando con CampusLands..........................................
            trainers()
        elif opcion==4: #Listar los campers que cuentan con bajo rendimiento.............................................
            rendimiento()
        elif opcion==5: #Listar los campers y trainers que se encuentren asociados a una ruta-------------------------------------------------------
            asociados()
        elif opcion==6: #Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos...............................................
            cantidad()
        elif opcion==0: #Salir....................................................................
            print("********************************")
            print("* Volviendo al menú principal  *")
            print("********************************")
        else:
            #Error para numeros
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        #Error para la opc
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")
<h2>Permanencia de datos usando los archivos .json</h2>
<p>Usamos la permanencia de datos con los archivos "rutas.json", "estudiantes.json" y "profesor.json" donde los ultimos dos solo los guardamos un diccionario adentro de una lista pero en "rutas.json" guardamos toda la informacion de varios diccionarios y listas adentro de una lista para despues ser mostrada al usuario dependiendo de lo que desee ver. Este es un ejemplo usando ese archivo "ruta.json"</p>
[
    {
        "nombre": "Fundamentos de programacion",
        "salon": {
            "1": {
                "trainer": [
                    {
                        "nombre": "Juan",
                        "apellido": "Carlos",
                        "tiempo": "dia"
                    }
                ],
                "tiempo": "dia",
                "capacidad": 33,
                "i": {
                    "camper": [
                        {
                            "nombre": "Camilo",
                            "apellido": "Navas",
                            "documento": "123456789",
                            "direccion": "Cra 9",
                            "acudiente": "Cris",
                            "telefono": "12345",
                            "estado": "inscrito",
                            "inicial": "Aprobado",
                            "rendimiento": "alto",
                            "riesgo": "bajo",
                            "atencion": "no",
                            "NotaFinal": 80.0,
                            "final": "Cursando"
                        },
                        {
                            "nombre": "Maria",
                            "apellido": "Medina",
                            "documento": "1235",
                            "direccion": "nose",
                            "acudiente": "rodolfo",
                            "telefono": "765",
                            "estado": "inscrito",
                            "inicial": "Aprobado",
                            "rendimiento": "alto",
                            "riesgo": "bajo",
                            "atencion": "no",
                            "NotaFinal": 90.0,
                            "final": "Cursando"
                        }
                    ]
                }
            },
            "2": {
                "trainer": []
            },
            "3": {
                "trainer": []
            }
        }
    }
]
