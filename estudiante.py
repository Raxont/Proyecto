import json
#Funcion para ingresar los datos de un camper ----------------------------------------
def regparticipantes():
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    d={
        "nombre":input("Ingrese el nombre del camper: "),
        "apellido":input("Ingrese el apellido del camper: "),
        "documento":input("Ingrese el # de documento del camper: "),
        "direccion":input("Ingrese la direccion del camper: "),
        "acudiente":input("Ingrese el nombre del acudiente del camper: "),
        "telefono":input("Ingrese el # de celular y # fijo del camper: "),
        "estado":"En proceso de ingreso",
        "inicial":"Aprobado",
        "rendimiento":"medio",
        "riesgo":"bajo",
        "atencion":"no"
    }
    estudiantes_info.append(d)

    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4) 

#Opciones del menu del camper --------------------------------------------------------
def opcc(opcion):
    if opcion == 1:
        regparticipantes()
    elif opcion == 0: 
        #Salir
        print("********************************")
        print("Volviendo al menú principal.")
        print("********************************")
    else:
        print("********************************")
        print("El valor no está en las opciones")
        print("********************************")



