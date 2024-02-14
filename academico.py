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
                            "1":{},
                            "2":{},
                            "3":{}
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
                        while salon!="1" and salon!="2" and salon!="3":
                            salon=int(input("Error, ingrese de nuevo el salon a cual va a ser asignado(1-3): "))
                        modulo=str(input("Ingrese el nombre del modulo: "))
                        if modulo in ruta_info:
                            print("Ya existe un modulo con el nombre del modulo a crear ")
                        else:    
                            horario=str(input("Ingrese el horario del modulo teniendo en cuenta que cada 4h hay clases [ejemplo(0-4)]: "))
                            capacidad=int(input("Ingrese la capacidad del modulo: "))
                            nuevo_modulo={
                                modulo:{
                                "horario":horario,
                                "capacidad":capacidad
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
            try:    
                with open('rutas.json', 'r') as ruta_file:
                    ruta_info = json.load(ruta_file)
                with open('profesor.json', 'r') as profe_file:
                    profe_info = json.load(profe_file)
                nombret=str(input("Ingrese el nombre del trainer: "))
                for i in profe_info:
                    if i['nombre'] == nombret:
                        nuevo_trainer["trainer"]=profe_info
                        print("Ingrese la ruta a la cual va a pertenecer el trainer ")
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
                                salon=str(input("Ingrese el salon del trainer(1-3): "))
                                while salon!="1" and salon!="2" and salon!="3":
                                    salon=int(input("Error, ingrese de nuevo el salon a cual va a ser asignado(1-3): "))
                                ruta_info[pos]["salon"][salon].update(nuevo_trainer)
                            else:
                                print(f"La ruta {opct} no esta registrada.")
                    else:
                        print(f"El trainer {nombret} no esta registrado.")
                with open ('rutas.json','w') as ruta_file:
                    json.dump(ruta_info, ruta_file, indent=4)
            except Exception as e:
                print("**************************")
                print("Ingrese una opción válida")
                print("**************************")
        elif opcion==5: #Asignar camper a una ruta -----------------------------------------
            nuevo_estudiante={}
            campers=[]
            try:
                with open('rutas.json', 'r') as ruta_file:
                    ruta_info = json.load(ruta_file)
                with open('estudiantes.json', 'r') as estudiantes_file:
                    estudiantes_info = json.load(estudiantes_file)
                nombre=str(input("Ingrese el nombre del camper a asignar una ruta: "))
                for i in estudiantes_info:
                    if i['nombre'] == nombre:
                        nuevo_estudiante["camper"]=campers.append(estudiantes_info)
                        print("Ingrese la ruta a la cual va a pertenecer el trainer ")
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
                                salon=str(input("Ingrese el salon del camper (1-3): "))
                                while salon!="1" and salon!="2" and salon!="3":
                                    salon=int(input("Error, ingrese de nuevo el salon del camper (1-3): "))
                                modulo=str(input("Ingrese el nombre del modulo a asignar: "))
                                if modulo in f["salon"][salon]:
                                    if i["inicial"]=="Aprobado":
                                        ruta_info[pos]["salon"][salon][modulo].update(nuevo_estudiante)
                                    else:
                                        print("El estudiante no aprobo el examen por lo tanto no puede continuar en el programa.")
                                else:
                                    print(f"El modulo {modulo} no esta reigstrado")
                    else:
                        print(f"El camper {nombre} no esta registrado.")
            except Exception as e:
                print(e)
                print("**************************")
                print("Ingrese una opción válida")
                print("**************************")
        elif opcion==6: #Registrar las notas del modulo
            notas.no()
        elif opcion==0: #Salir ---------------------------------
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
