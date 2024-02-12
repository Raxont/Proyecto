import menus
import confirmarsalida
#Funcion para ingresar los datos de un trainer ----------------------------------------
def regtrainer(trainer,campus):
    nombre=str(input("Ingrese el nombre del trainer: "))
    apellido=str(input("Ingrese el apellido del trainer: "))
    horario=int(input("Ingrese la cantidad de horas a trabajar(0-24)h :"))
    while horario<0 or horario>24:
        horario=int(input("Error, la cantidad de horas a trabajar nuevamente(0-24)h :"))
    tiempo=str(input("El horario es en la mañana?(s/n) :"))
    d={
        "nombre":nombre,
        "apellido":apellido,
        "horas":horario,
        "tiempo":tiempo,
    }
    trainer.append(d)
    if tiempo==True:
        campus["trainer"]=trainer
    return trainer,campus

#Opciones del menu del trainer --------------------------------------------------------
def gestion_participantes(opcion,trainer,campus):
    try:    
        if opcion == 1:
            regtrainer(trainer,campus)
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