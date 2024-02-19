import json
import menus
def no(): #Notas finales.......................................................................
    try:
        with open('rutas.json', 'r') as ruta_file:
            ruta_info = json.load(ruta_file)
        with open('estudiantes.json', 'r') as estudiantes_file:
            estudiantes_info = json.load(estudiantes_file)
        nombre=str(input("Ingrese el nombre del camper: "))
        bandera=False
        for estudiante in estudiantes_info:
            if estudiante['nombre'] == nombre:
                bandera=True
                print("Ingrese la ruta a la cual pertenece el camper:")
                opct = menus.menuRutas()
                if 1 <= opct <= 5:
                    opct_dict = {
                        1: "Fundamentos de programacion",
                        2: "Programacion Web",
                        3: "Programacion formal",
                        4: "Bases de datos",
                        5: "Backend"
                    }
                    opct_nombre = opct_dict[opct]
                    for i, ruta in enumerate(ruta_info):
                        if ruta['nombre']==opct_nombre:
                            salon = input("Ingrese el salon del camper (1-3): ")
                            while salon not in ["1", "2", "3"]:
                                salon = input("Error, ingrese de nuevo el salon del camper (1-3): ")
                            modulo = input("Ingrese el nombre del modulo que pertenece el camper: ")
                            if modulo in ruta["salon"][salon]: 
                                for f in ruta["salon"][salon][modulo]["camper"]:
                                    if f["nombre"]==nombre:
                                        teorica=float(input("Ingrese la nota teorica: "))
                                        practica=float(input("Ingrese la nota practica: "))
                                        trabajo=float(input("Ingrese la nota de los trabajos y quizes: "))
                                        total=(teorica*0.3)+(practica*0.6)+(trabajo*0.1)
                                        if total>=60:
                                            f["final"]="Cursando"
                                            if total>=60 and total<70: 
                                                f["rendimiento"]="bajo"
                                                f["riesgo"]="alto"
                                                f["atencion"]="si"
                                            elif total>=70 and total<90:
                                                f["rendimiento"]="medio"
                                                f["riesgo"]="medio"
                                                f["atencion"]="no"
                                            elif total>=90:
                                                f["rendimiento"]="alto"
                                                f["riesgo"]="bajo"
                                                f["atencion"]="no"
                                        else:
                                            f["final"]="Expulsado"
                                            f["rendimiento"]="bajo"
                                            f["riesgo"]="alto"
                                            f["atencion"]="si"
                                        f["NotaFinal"]=total 
                                        print("***********************************")
                                        print("* Notas registradas correctamente *")
                                        print("***********************************")
                                        print("\nRegresando al menu...")
                                        break
                                else:
                                    print(f"\nEl camper {nombre} no se encontró registrado en el modulo.")
                            else:
                                print(f"\nEl modulo {modulo} no esto registrado.")
                            break
                    else:
                        print(f"\nLa ruta {opct_nombre} no está registrada.")
                else:
                    print("\nOpcion incorrecta")
                break
        if not bandera:
            print(f"\nEl camper {nombre} no está registrado en la base de datos.")
        with open('rutas.json', 'w') as ruta_file:
            json.dump(ruta_info, ruta_file, indent=4)
    except Exception as e:
        print("*****************************")
        print("* Ingrese una opción válida *")
        print("*****************************")

            
def notar(): #Notas iniciales..................................................................................
    encontradonombre=1
    nombre=str(input("Ingrese el nombre del camper a registrar las notas: "))
    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_info = json.load(estudiantes_file)
    for i in estudiantes_info:
        if i["nombre"]==nombre:
            teorica=float(input("Ingrese la nota teorica: "))
            practica=float(input("Ingrese la nota practica: "))
            total=(teorica+practica)/2
            if total>=60:
                i["inicial"]="Aprobado"
                i["estado"]="inscrito"
                if total>=60 and total<=70:  
                    i["rendimiento"]="bajo"
                    i["riesgo"]="alto"
                    i["atencion"]="si"
                elif total<70 and total<90:
                    i["rendimiento"]="medio"
                    i["riesgo"]="medio"
                    i["atencion"]="no"
                elif total>=90:
                    i["rendimiento"]="alto"
                    i["riesgo"]="bajo"
                    i["atencion"]="no"
            else:
                i["estado"]="Expulsado"
                i["inicial"]="No aprobado"
                i["riesgo"]="alto"
                i["atencion"]="si"
            encontradonombre=1
            i["NotaFinal"]=total
            print("***********************************")
            print("* Notas registradas correctamente *")
            print("***********************************")
            print("\nRegresando al menu...")
        else:
            encontradonombre=0    
    if encontradonombre==1:
        print("")
    elif encontradonombre==0:
        print(f"El camper {nombre} no se encontró registrado.")
        print("Volviendo al menu...")

    with open ('estudiantes.json','w') as estudiantes_file:
        json.dump(estudiantes_info, estudiantes_file, indent=4)