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