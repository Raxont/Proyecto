def imp(opcion,camper,trainer,campus):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    try:
        if opcion==1:
            for i in camper:
                if i["estado"]=="inscrito":
                    print(f""" Los estudiantes inscritos son
                          ----- El estudiante #{c1+1}
                          Su nombre es {i["nombre"]}
                          Su apellido es{i["apellido"]}
                          Su numero de documento es {i["documento"]}
                          Su direccion es {i["direccion"]}
                          El nombre de su acudiente es {i["acudiente"]}
                          El numero de telefono es {i["telefono"]}
                          Con un rendimiento {i["rendimiento"]}
                          Con un riesgo {i["riesgo"]}
                          Tiene llamado de atencion? {i["atencion"]}
                          """)
        elif opcion==2:
            for i in camper:
                if i["inicial"]=="Aprobado":
                    print(f""" Los estudiantes con el examen inicial aprobado son 
                          ----- El estudiante #{c2+1}
                          Su nombre es {i["nombre"]}
                          Su apellido es{i["apellido"]}
                          Su numero de documento es {i["documento"]}
                          Su direccion es {i["direccion"]}
                          El nombre de su acudiente es {i["acudiente"]}
                          El numero de telefono es {i["telefono"]}
                          Con un rendimiento {i["rendimiento"]}
                          Con un riesgo {i["riesgo"]}
                          Tiene llamado de atencion? {i["atencion"]}
                          """)
        elif opcion==3:
            for i in trainer:
                print(f""" Los trainers inscritos son 
                          ----- El trainer #{c3+1}
                          Su nombre es {i["nombre"]}
                          Su apellido es{i["apellido"]}
                          Horas a trabajar{i["horas"]}
                          Trabaja en la mañana?{i["tiempo"]}
                          """)
        elif opcion==4:
            for i in camper:
                if i["rendimiento"]=="bajo":
                    print(f""" Los estudiantes con rendimiento bajo son 
                          ----- El estudiante #{c4+1}
                          Su nombre es {i["nombre"]}
                          Su apellido es{i["apellido"]}
                          Su numero de documento es {i["documento"]}
                          Su direccion es {i["direccion"]}
                          El nombre de su acudiente es {i["acudiente"]}
                          El numero de telefono es {i["telefono"]}
                          Con un riesgo {i["riesgo"]}
                          Tiene llamado de atencion? {i["atencion"]}
                          """)
        elif opcion==5:
            runta=str(input("Ingrese cual ruta desea buscar: "))
            if campus["ruta"]==runta:
                print(f"""
                        El trainer encargado de la ruta es {trainer}
                        """)
            

    except:
        print("")
    