def regparticipantes(camper,campus):
    d={
        "nombre":str(input("Ingrese el nombre del camper: ")),
        "apellido":str(input("Ingrese el apellido del camper: ")),
        "documento":str(input("Ingrese el # de documento del camper: ")),
        "direccion":str(input("Ingrese la direccion del camper: ")),
        "acudiente":str(input("Ingrese el nombre del acudiente del camper: ")),
        "telefono":str(input("Ingrese el # de celular y # fijo del camper: ")),
        "estado":"En proceso de ingreso",
        "riesgo":"Ninguno"
    }
    camper.append(d)
    campus["camper"]=camper
    return camper,campus

def opcioncamper(opcion,camper,campus):
    if opcion == 1:
        regparticipantes(camper,campus)
    else: 
        print("********************************")
        print("El valor no está en las opciones")
        print("********************************")