def regtrainer(trainer,campus):
    d={
        "nombre":str(input("Ingrese el nombre del trainer: ")),
        "apellido":str(input("Ingrese el apellido del trainer: ")),
        "horario":str(input("Ingrese el horario del trainer: ")),
    }
    trainer.append(d)
    campus["trainer"]=trainer
    return trainer,campus

def gestion_participantes(opcion,trainer,campus):
    if opcion == 1:
        regtrainer(trainer,campus)
    else: 
        print("********************************")
        print("El valor no está en las opciones")
        print("********************************")