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

