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
            with open('rutas.json', 'r') as ruta_file:
                ruta_info = json.load(ruta_file)
            menus.menuRutas()
            nombreruta=str(input("Ingrese el nombre de la ruta a crear: "))
            if nombreruta in ruta_info:
                print("Ya existe una ruta con la nombre de la ruta a crear ")
            else:    
                nueva_ruta = {
                "nombre":nombreruta,
                "salon":{
                            "1":{"trainer":[]},
                            "2":{"trainer":[]},
                            "3":{"trainer":[]}
                        }
                    }
                ruta_info.append(nueva_ruta)
                with open ('rutas.json','w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4) 
        elif opcion==3:#Crear los modulos de las rutas y su horario ------------------------------------------------
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
                            horario=str(input("Ingrese el horario del modulo teniendo en cuenta que cada 4h hay clases [ejemplo(0-4)]: "))
                            capacidad=int(input("Ingrese la capacidad del modulo: "))
                            nuevo_modulo={
                                modulo:{
                                "horario":horario,
                                "capacidad":capacidad,
                                "camper":[]
                                }
                            }
                            ruta_info[pos]["salon"][salon].update(nuevo_modulo)
                with open ('rutas.json','w') as ruta_file:
                        json.dump(ruta_info, ruta_file, indent=4)
            except Exception as e:
                print("**************************")
                print("Ingrese una opción válida")
                print("**************************")
        elif opcion==4: #Ingresar un trainer a un salon ---------------------------------
            nuevo_trainer = {}
            verificar=0
            encontrarnombre=1
            encontradoruta=1
            encontraropcion=1
            encontradoregistro=1
            try:    
                with open('rutas.json', 'r') as ruta_file:
                    ruta_info = json.load(ruta_file)
                with open('profesor.json', 'r') as profe_file:
                    profe_info = json.load(profe_file)
                nombret=str(input("Ingrese el nombre del trainer: "))
                for i in profe_info:
                    if i['nombre'] == nombret:
                        postrainer=profe_info.index(i)
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
                                    while salon not in["1","2","3"]:
                                        salon=int(input("Error, ingrese de nuevo el salon del trainer (1-3): "))
                                    for x in f["salon"][salon]["trainer"][postrainer]:
                                        if nombret in x["nombre"]:
                                            verificar=verificar+1
                                    if verificar==0:     
                                        ruta_info[pos]["salon"][salon]["trainer"].append(i)
                                        print("Trainer agregado exitosamente.")
                                        encontrarnombre=1
                                        encontradoruta=1
                                        encontraropcion=1
                                        encontradoregistro=1
                                        break
                                    else:
                                        encontradoregistro=0
                                        encontrarnombre=1
                                        encontradoruta=1
                                        encontraropcion=1
                                        break
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
                        encontradonombre=0
                
                if encontradonombre==1:
                    if encontraropcion==1:    
                        if encontradoruta==1:
                            if encontradoregistro==1:
                                print("")
                            elif encontradoregistro==0:
                                print(f"El trainer {nombret} ya esta asignado a este modulo")    
                        elif encontradoruta==0:
                            print(f"La ruta {opct} no esta registrada.")
                    elif encontraropcion==0:
                        print("Opción incorrecta") 
                elif encontradonombre==0:    
                    print(f"El trainer {nombret} no esta registrado.")  
                
                with open ('rutas.json','w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
            except Exception as e:
                print("**************************")
                print("Ingrese una opción válida")
                print("**************************")
        elif opcion==5: #Asignar camper a una ruta -----------------------------------------
            with open('rutas.json', 'r') as ruta_file:
                ruta_info = json.load(ruta_file)
            with open('estudiantes.json', 'r') as estudiantes_file:
                estudiantes_info = json.load(estudiantes_file)
            bandera = str(input("Desea empezar a agregar estudiantes? (s/n): ")).lower()
            while bandera == "s":
                agregar_estudiante(estudiantes_info,ruta_info)
                with open('rutas.json', 'w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
                bandera = str(input("Desea continuar agragando estudiantes? (s/n): ")).lower()
                while bandera != "s" and bandera != "n":
                    bandera = str(input("Error, indique si desea continuar agregando campers? (s/n): ")).lower()
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
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")

def agregar_estudiante(estudiantes_info, ruta_info):
    nuevo_estudiante = {}
    camperss = []
    verificar=0
    encontradomodulo=1
    encontradonombre=1
    encontradoruta=1
    encontradoinicial=1
    encontradoregistro=1
    encontradopcion=1
    try:
        nombre = str(input("Ingrese el nombre del camper a asignar una ruta: "))
        for i in estudiantes_info:
            if i['nombre'] == nombre:
                print("Ingrese la ruta a la cual va a pertenecer el camper ")
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
                            modulo = str(input("Ingrese el nombre del modulo a asignar: "))
                            if modulo in f["salon"][salon]:
                                if i["inicial"] == "Aprobado":
                                    for x in f["salon"][salon][modulo]["camper"]:
                                        if nombre in x["nombre"]:
                                            verificar=verificar+1
                                    if verificar==0:    
                                        ruta_info[pos]["salon"][salon][modulo]["camper"].append(i)
                                        print("Estudiante agregado exitosamente.")
                                        encontradomodulo=1
                                        encontradonombre=1
                                        encontradoruta=1
                                        encontradoinicial=1
                                        encontradoregistro=1
                                        encontradopcion=1
                                        break
                                    else:
                                        encontradomodulo=1
                                        encontradonombre=1
                                        encontradoruta=1
                                        encontradoinicial=1
                                        encontradopcion=1
                                        encontradoregistro=0
                                        break
                                else:
                                    encontradomodulo=1
                                    encontradoruta=1
                                    encontradoinicial=0
                                    encontradoregistro=0
                                    encontradopcion=1
                                    encontradonombre=1
                            else:
                                encontradomodulo=0
                                encontradoruta=1
                                encontradoinicial=0
                                encontradoregistro=0
                                encontradopcion=1
                                encontradonombre=1
                        else:
                            encontradomodulo=0
                            encontradoruta=0
                            encontradoinicial=0
                            encontradoregistro=0
                            encontradopcion=1
                            encontradonombre=1
                else:    
                    encontradomodulo=0
                    encontradoruta=0
                    encontradoinicial=0
                    encontradoregistro=0
                    encontradopcion=0
                    encontradonombre=1
            else:
                encontradomodulo=0
                encontradoruta=0
                encontradoinicial=0
                encontradoregistro=0
                encontradopcion=0
                encontradonombre=0

        if encontradonombre==1:
            if encontradopcion==1:
                if encontradoruta==1:
                    if encontradomodulo==1:
                        if encontradoinicial==1:
                            if encontradoregistro==1:
                                print("")
                            elif encontradoregistro==0:    
                                print(f"El camper {nombre} ya esta asignado a este modulo")
                                print("")    
                        elif encontradoinicial==0:
                            print(f"El camper {nombre} no aprobo el examen por lo tanto no puede continuar en el programa.")    
                    elif encontradomodulo==0:    
                        print(f"El modulo {modulo} no esta registrado.") 
                elif encontradoruta==0:
                    print(f"La ruta {opct} no esta registrada.")
            elif encontradopcion==0:
                print("Opción incorrecta")        
        elif encontradonombre==0:    
            print(f"El camper {nombre} no esta registrado.")    
           
    except Exception as e:
        print(e)
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")