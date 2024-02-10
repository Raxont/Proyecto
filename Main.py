import imprimir
import confirmarsalida
import camper
import coordinador
import menus
import trainer
#Programa para llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
camper=[]
trainer={}
campus={}
while True:
    try:
        opc = menus.menuPrincipal()
        if opc == 1:
            #Menu Coordinador
            clave=input("Ingrese la clave del coordinador para ingresar: ")
            if clave=="1":
               opcCorrdinador=menus.menuCoordinador(camper)
               coordinador.m(opcCorrdinador,camper)
            else:
                print("Clave incorrecta")
        elif opc == 2:
            #Menu Trainer
            clave=input("Ingrese la clave del Trainer para ingresar: ")
            if clave=="2":
                opcp = menus.menuTrainer()
                trainer.regtrainer(opcp,camper,campus)
            else:
                print("Clave incorrecta")
        elif opc == 3:
            #Menu Camper
            opcp = menus.menuParticipantes()
            camper.opcioncamper(opcp)
        elif opc == 0:
            #Salir
            if confirmarsalida.salida():
                break
        else:
            #Error para numeros
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        #Error para la opc
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")