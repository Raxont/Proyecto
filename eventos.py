#Registrar eventos
def regeventos():
    nombre=str(input("Ingrese el nombre del evento "))
    
    d={
        "nombre":nombre,
        "locacion":str(input("Ingrese la locacion del evento ")),
        "dia":str(input("Ingrese el dia del evento ")),
      }
    return d

#Modificar los eventos
def m(dic):
    print("""Ingrese que desea modificar del evento
        1) Nombre
        2) Lugar
        3) Dia
          """)
    opcion=int(input("Ingrese una opcion: "))
    try:
        if opcion==1:
            dic["nombre"]=str(input("Ingrese el nuevo nombre del evento: "))
            return dic
        elif opcion==2:
            dic["locacion"]=str(input("Ingrese la nueva locacion del evento: "))
            return dic
        elif opcion==3:
            dic["dia"]=str(input("Ingrese el nuevo dia del evento: "))
            return dic
        else:
            print("Opcion no valida, ingrese una opcion valida(1-3)")
    except:
        print("Opcion no valida, ingrese una opcion valida(1-3)")
#Quitar eventos
def quitar(nombre,evento):
    if nombre == evento["nombre"]:
        evento.clear()
        print(f"El evento {nombre} fue eliminado... ")
        return
    else:
        print(f"El evento {nombre} no se encontró.")

