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