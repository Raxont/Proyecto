import json
def no():
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    with open('rutas.json', 'r') as ruta_file:
        ruta_info = json.load(ruta_file)
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    for i in estudiantes_info:
        if nombre == i["nombre"]:
            posicion=estudiantes_info.index(i)
            teorica=float(input("Ingrese la nota teorica"))
            practica=float(input("Ingrese la nota practica"))
            trabajo=float(input("Ingrese la nota de los trabajos y quizes"))
            total=(teorica*0.3)+(practica*0.6)+(trabajo*0.1)
            if total>=60:
                i[posicion]["estado"]="Cursando"
                if total>=60 and total<70: 
                    i["rendimiento"]="bajo"
                    i["riesgo"]="alto"
                    i["atencion"]="si"
                elif total>90:
                    i["rendimiento"]="alto"
                    i["riesgo"]="bajo"
                    i["atencion"]="no"
            else:
                i["estado"]="Expulsado"
                i["rendimiento"]="Bajo"
                i["riesgo"]="alto"
                i["atencion"]="si"
            i["NotaInicial"]=total
            estudiantes_info=i    
        else:    
            print(f"El camper {nombre} no se encontró registrado.")
    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4)
    with open ('rutas.json','w') as ruta_file:
        json.dump(ruta_info, ruta_file, indent=4)
            
def notar():
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    with open('rutas.json', 'r') as ruta_file:
        ruta_info = json.load(ruta_file)
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    for i in estudiantes_info:
        if i["nombre"]==nombre:
            posicion=estudiantes_info.index(i)
            teorica=float(input("Ingrese la nota teorica "))
            practica=float(input("Ingrese la nota practica "))
            total=(teorica+practica)/2
            if total>=60:
                i["inicial"]="Aprobado"
                i["estado"]="inscrito"
                if total>=60 and total<70:  
                    i["rendimiento"]="bajo"
                    i["riesgo"]="alto"
                    i["atencion"]="si"
                elif total>90:
                    i["rendimiento"]="alto"
                    i["riesgo"]="bajo"
                    i["atencion"]="no"
            else:
                i["inicial"]="No aprobado"
                i["estado"]="Expulsado"
                i["riesgo"]="alto"
                i["atencion"]="si"
            i["NotaFinal"]=total
            estudiantes_info=i
        else:    
            print(f"El camper {nombre} no se encontró registrado.")
    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4)
    with open ('rutas.json','w') as ruta_file:
        json.dump(ruta_info, ruta_file, indent=4)