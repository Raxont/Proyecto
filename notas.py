def no(camper):
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    for i in camper:
        if nombre == i["nombre"]:
            posicion=camper.index(i)
            teorica=float(input("Ingrese la nota teorica"))
            practica=float(input("Ingrese la nota practica"))
            trabajo=float(input("Ingrese la nota de los trabajos y quizes"))
            total=(teorica*0.3)+(practica*0.6)+(trabajo*0.1)
            if total>=60:
                camper[posicion]["estado"]="Inscrito"
                if total>=60 and total<70: 
                    camper[posicion]["rendimiento"]="bajo"
                    camper[posicion]["riesgo"]="alto"
                    camper[posicion]["atencion"]="si"
                elif total>90:
                    camper[posicion]["rendimiento"]="alto"
                return camper
            else:
                camper[posicion]["estado"]="No Inscrito"
                camper[posicion]["rendimiento"]="Bajo"
                camper[posicion]["riesgo"]="alto"
                camper[posicion]["atencion"]="si"
                return camper
        else:    
            print(f"El camper {nombre} no se encontró registrado.")
            
def notar(camper):
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    for i in camper:
        if nombre == i["nombre"]:
            posicion=camper.index(i)
            teorica=float(input("Ingrese la nota teorica"))
            practica=float(input("Ingrese la nota practica"))
            total=(teorica+practica)/2
            if total>=60:
                camper[posicion]["inicial"]="Aprobado"
                camper[posicion]["estado"]="inscrito"
                if total>=60 and total<70:  
                    camper[posicion]["rendimiento"]="bajo"
                    camper[posicion]["riesgo"]="alto"
                    camper[posicion]["atencion"]="si"
                elif total>90:
                    camper[posicion]["rendimiento"]="alto"
                return camper
            else:
                camper[posicion]["inicial"]="No aprobado"
                camper[posicion]["estado"]="Expulsado"
                return camper
        else:    
            print(f"El camper {nombre} no se encontró registrado.")