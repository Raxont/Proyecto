import menus
import json
import confirmarsalida
#Funcion para ingresar los datos de un trainer ----------------------------------------
def regtrainer():
    with open('profesor.json', 'r') as profe_file:
        profe_info = json.load(profe_file)
    nombre=str(input("Ingrese el nombre del trainer: "))
    apellido=str(input("Ingrese el apellido del trainer: "))
    tiempo=str(input("ingrese el horario del profesor(dia,tarde,noche): ")).lower()
    while tiempo!="dia" and tiempo!="tarde" and tiempo!="noche":
        tiempo=str(input("Error, debe digitar una opcion indicada(dia,tarde,noche): ")).lower()
    d={
        "nombre":nombre,
        "apellido":apellido,
        "tiempo":tiempo
    }
    profe_info.append(d)
    print("*************************************")
    print("* Profesor agregado correctamente *")
    print("*************************************")
    print("")
    print("Regresando al menu...")
    with open ('profesor.json','w') as profe_file:
        json.dump(profe_info, profe_file, indent=4) 

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