#Funcion para ingresar los datos de un camper
def regparticipantes(camper,campus):
    d={
        "nombre":str(input("Ingrese el nombre del camper: ")),
        "apellido":str(input("Ingrese el apellido del camper: ")),
        "documento":str(input("Ingrese el # de documento del camper: ")),
        "direccion":str(input("Ingrese la direccion del camper: ")),
        "acudiente":str(input("Ingrese el nombre del acudiente del camper: ")),
        "telefono":str(input("Ingrese el # de celular y # fijo del camper: ")),
        "estado":"En proceso de ingreso",
        "riesgo":"Inscrito"
    }
    camper.append(d)
    campus["camper"]=camper
    return camper,campus

#Funcion para las opciones del menu de campers
def opcioncamper(opcion,camper,campus):
    if opcion == 1:
        regparticipantes(camper,campus)
    else: 
        print("********************************")
        print("El valor no está en las opciones")
        print("********************************")

# Función para inscribir a un camper en una ruta
def inscribir(ncamper,nruta,campers,rutas):
    camper=campers[ncamper]
    ruta=rutas[nruta]
    if len(ruta['sala']['campers']) < ruta['sala']['capacidad']:
        camper['rutas'].append(ruta_id)
        ruta['sala']['campers'].append(camper_id)
        camper['inscrito'] = True
        print(f"El camper {camper['name']} se ha inscrito en la ruta {ruta['name']}.")
    else:
        print("La sala de entrenamiento está llena.")