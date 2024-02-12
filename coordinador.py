import camper
import rutas
import menus
import confirmarsalida
#Opciones del menu del coordinador --------------------------------------------------------
def m(opcion,camper,campus):
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
                        camper[posicion]["estado"]="Aprobado"
                        return camper
                    else:
                        camper[posicion]["estado"]="No aprobado"
                        return camper
            print(f"El camper {nombre} no se encontró registrado.")
        elif opcion==2: #Ingresar un trainer a un salon ---------------------------------
            nombret=str(input("Ingrese el nombre del trainer: "))
            for i in campus["trainer"]:
                if nombret==i["nombre"]:
                    posicion=camper.index(i)
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
            print(f"El trainer {nombre} no esta registrado.")
        elif opcion==3: #Asignar camper a una ruta -----------------------------------------
            nombre=str(input("Ingrese el nombre del camper a asignar una ruta: "))   
            for i in camper:
                if nombre == i["nombre"]:
                    if i["estado"]=="Aprobado":
                        opruta=menus.menuRutas()
                        posicion=camper.index(i)
                        if opruta==1:
                            camper.inscribir(posicion,'Fundamentos de programación',camper[posicion],campus["trainer"][posicion1])
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
    except:
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")
