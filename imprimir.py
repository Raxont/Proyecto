def imp(d,c):
    try:
        print("\rEl nombre del evento es: ",d["nombre"])
        print("El lugar del evento es: ",d["locacion"])
        print("El dia del evento es: ",d["dia"])
    except:
        print("\rNo se han registrado eventos")
    finally:
        try:     	
            for i in range(c):  
                print(f"\r\rLos datos del participante #{i+1} es: \nEl nombre es: {d["persona"][i]["nombre"]}")
                print("El documento es: ",d["persona"][i]["documento"])
                print("La edad es: ",d["persona"][i]["edad"])
                print("El cargo es: ",d["persona"][i]["cargo"])
                print("El participante tiene una deuda? ",d["persona"][i]["deuda"])
                print("La deuda del participante es: $",d["persona"][i]["costo"],"cop")
        except:
            print("\rNo se han registrado mas participantes")  
        finally:
            try:
                print("")
                print(f"\r\rEl nombre de los participantes con deudas es: ")
                for i in range(c): 
                    if d["persona"][i]["deuda"]=="Si":
                        print(d["persona"][i]["nombre"])
                        print("")
            except:
                print("No hay mas participantes con deudas")  
