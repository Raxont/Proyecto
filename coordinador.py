#Registrar las notas de un camper
def m(opcion,camper):
    try:
        if opcion==1:
            nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
            for i in camper:
                if nombre == i["nombre"]:
                    posicion=camper.index(i)
                    teorica=float(input("Ingrese la nota teorica"))
                    practica=float(input("Ingrese la nota practica"))
                    total=(teorica*total)/2
                    if total>=60:
                        camper[posicion]["estado"]="Aprobado"
                        return camper
                    else:
                        camper[posicion]["estado"]="No aprobado"
                        return camper
            print(f"El participante {nombre} no se encontró en ningún evento.")
        else:
            print("Opcion no valida, ingrese una opcion valida(1-3)")
    except:
        print("Opcion no valida, ingrese una opcion valida(1-3)")
