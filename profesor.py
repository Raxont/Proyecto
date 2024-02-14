import menus
import json
import confirmarsalida
#Funcion para ingresar los datos de un trainer ----------------------------------------
def regtrainer():
    with open('profesor.json', 'r') as profe_file:
        profe_info = json.load(profe_file)
    nombre=str(input("Ingrese el nombre del trainer: "))
    apellido=str(input("Ingrese el apellido del trainer: "))
    horario=int(input("Ingrese la cantidad de horas a trabajar(0-24)h :"))
    while horario<0 or horario>24:
        horario=int(input("Error, la cantidad de horas a trabajar nuevamente(0-24)h :"))
    tiempo=str(input("El horario es en la mañana?(s/n) :")).lower()
    while tiempo!="s" and tiempo!="n":
        tiempo=str(input("Error, debe digitar una opcion indicada(s/n) :")).lower()
    d={
        "nombre":nombre,
        "apellido":apellido,
        "horas":horario,
    }
    if tiempo=="s":
        profe_info.append(d)
        with open ('profesor.json','w') as profe_file:
            json.dump(profe_info, profe_file, indent=4) 
    elif tiempo=="n":
        print("Lo lamentamos, solo necesitamos trainers en la mañana")

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