import imprimir
import confirmarsalida
import eventos
import participantes
import menus
#Programa para llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
evento={}
persona=[]
cont=0
p=0

while True:
    try:
        opc = menus.menuPrincipal()
        if opc == 1:
            #Menu eventos
            menus.menuEventos()
        elif opc == 2:
            #Menu participantes
            opcp = menus.menuParticipantes()
            participantes.regparticipantes(opcp)
        elif opc == 0:
            #Salir
            if confirmarsalida.salida():
                break
        else:
            #Error para numeros
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        #Error para la opc
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")

"""while True:
    #Menu 
    print(""        ----------- Menu -------------------
        1) 
        2) Quitar participante
        3) Registrar Evento
        ------------------------------------  "")
    try:    
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1: #Registrar participantes
            participantes.regparticipantes(persona,evento)
            cont+=1
        elif opcion==2: #Eliminar participantes
            p=str(input("Ingrese el nombre del participante: "))
            quitarp.quitar(p,persona)
        elif opcion==3: #Registrar evento
            evento=eventos.regeventos()
        elif opcion==4: #Modificar evento
            modificar.m(evento)
        elif opcion==5: #Quitar evento
            nombre=input("Ingrese el nombre del evento: ")
            quitare.quitar(nombre,evento)
        elif opcion==6: #Mostrar datos de registros
            imprimir.imp(evento,cont)
        elif opcion==7: #Salir
            if confirmarsalida.salida():
                break
        else: #Error para numeros
            print("Opcion no valida, ingrese una opcion valida(1-7)")
    except: #Error para caracteres
        print("Opcion no valida")"""