def regparticipantes(p,eventos):
    d={
        "nombre":str(input("Ingrese el nombre del participante: ")),
        "documento":str(input("Ingrese el documento del participante: ")),
        "edad":str(input("Ingrese la edad del participante: ")),
        "cargo":str(input("Ingrese el cargo del participante: ")),
        "dinero":int(input("Ingrese cuanto dinero va a pagar: $"))
    }
    while d["dinero"]>50000:
        d["dinero"]=int(input("El dinero no puede ser mayor a $50.000 COP, ingrese cuanto dinero va a pagar: $"))
    if d["dinero"]<50000:
        d["deuda"]="Si"
        d["costo"]=50000-d["dinero"]
    elif d["dinero"]==50000:
        d["deuda"]="No"
        d["costo"]=0
    p.append(d)
    eventos["persona"]=p
    
    return p,eventos

def quitar(nombre,persona):
    posicion=0
    for i in persona:
        if i["dinero"]==0 and nombre == i["nombre"]:    
            posicion=persona.index(i)
            del persona[posicion]
            print(f"El participante {nombre} fue eliminado del evento")
            return   
    print(f"El participante {nombre} no se encontró en ningún evento o no puede pedir devoluciones al ya tener pago el evento")

def gestion_participantes(opcion):
    if opcion == 1:
        regparticipantes()
    if opcion == 2:
        eliminar_participante()
    if opcion == 3:
        participantes_que_no_han_cancelado()
    if opcion == 4:
        deuda_participantes()
    else: 
        print("********************************")
        print("El valor no está en las opciones")
        print("********************************")