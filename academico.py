import rutas
import menus
import confirmarsalida
#Opciones del menu del coordinador --------------------------------------------------------
def m(opcion,camper,trainer,campus):
    try:
        if opcion==1: #Registrar notas del camper ------------------------------------------
            nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
            for i in camper:
                if nombre == i["nombre"]:
                    posicion=camper.index(i)
                    teorica=float(input("Ingrese la nota teorica"))
                    practica=float(input("Ingrese la nota practica"))
                    total=(teorica*total)/2
                    if total>=60:
                        camper[posicion]["estado"]="Inscrito"
                        return camper
                    else:
                        camper[posicion]["estado"]="No Inscrito"
                        return camper
                else:    
                    print(f"El camper {nombre} no se encontró registrado.")
        elif opcion==2: #Ingresar un trainer a un salon ---------------------------------
            nombret=str(input("Ingrese el nombre del trainer: "))
            for i in trainer:
                if nombret == i["nombre"]:
                    posicion=trainer.index(i)
                    print("Ingrese la ruta a la cual va a pertenecer el trainer ")
                    opct=menus.menuRutas()
                    salon=int(input("Ingrese el salon a cual va a ser asignado(1-3): "))
                    if opct==1:
                        campus["rutas"]["Fundamentos de programación"][salon]["trainers"]=i
                    elif opct==2:
                        campus["rutas"]["Programación Web"][salon]["trainers"]=i
                    elif opct==3:
                        campus["rutas"]["Programación formal"][salon]["trainers"]=i
                    elif opct==4:
                        campus["rutas"]["Bases de datos"][salon]["trainers"]=i
                    elif opct==5:
                        campus["rutas"]["Backend"][salon]["trainers"]=i
                    else:
                        print("Opcion incorrecta")
                else:
                    print(f"El trainer {nombret} no esta registrado.")
        elif opcion==3: #Asignar camper a una ruta -----------------------------------------
            nombre=str(input("Ingrese el nombre del camper a asignar una ruta: "))
            salon=int(input("Ingrese el salon del camper (1-3): "))
            while salon!=1 and salon!=2 and salon!=3:
                salon=int(input("Error, ingrese de nuevo el salon del camper (1-3): "))
            hora=int(input("""Ingrese la hora de la ruta
                           1) 0-4
                           2) 4-8
                           3) 8-12
                           :"""))
            while hora!=1 and hora!=2 and hora!=3:
                hora=int(input("""Error, ingrese de nuevo la hora de la ruta
                           1) 0-4
                           2) 4-8
                           3) 8-12
                           :"""))   
            for i in camper:
                if nombre == i["nombre"]:
                    if i["estado"]=="Aprobado":
                        opruta=menus.menuRutas()
                        posicion=camper.index(i)
                        if opruta==1:
                            inscribir(camper[posicion],'Fundamentos de programación',salon,campus,hora)
                    else:
                        print("El estudiante no aprobo el examen por lo tanto no puede continuar en el programa.")
            print(f"El camper {nombre} no esta registrado.")
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

# Función para inscribir a un camper en una ruta --------------------------------------
def inscribir(camper,nruta,salon,campus,hora):
    rutaa=campus["rutas"][nruta][salon][hora]
    if len(rutaa["campers"]) < rutaa["capacidad"]:
        camper["ruta"].append(nruta)
        campus["rutas"][nruta][salon][hora]["campers"].append(camper)
        camper['estado'] = "Aprobado"
        print(f"El camper {camper["nombre"]} se ha inscrito en la ruta {nruta}.")
    else:
        print("La sala de entrenamiento está llena.")

