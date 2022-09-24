sillas_total = 5                                                                          
cola_sillas = 0
cliente = 0
sillas_ocupadas = 0      
                                             

def Opcion_cliente (cola):
    opcion = {                                                                      
        1 : estado_barberia,
        2 : llegada_clientes,
        3 : barberia_vacia
    }
    func = opcion.get (cola,)
    return func ()

def llegada_clientes ():
    global sillas_ocupadas
    if sillas_ocupadas == 0:                                                                 
        print("\nEl barbero está dormido.")
        global cliente
        cliente = (cliente + 1) % sillas_total
        sillas_ocupadas +=1
        print("El primer cliente entra.")

    elif sillas_ocupadas == sillas_total:                                                          
        print("\nTodas las sillas estan ocupadas.")
        print("El nuevo cliente se va.")
    
    else:                                                                          
        cliente = (cliente + 1) % sillas_total
        sillas_ocupadas += 1
        print("\nEl cliente que llego se sienta.")
        print("Hay sillas disponibles.")

    elegir_opciones ()

def estado_barberia ():                                                                 
    caso_cliente = 1                                                                           
    print ("\n|", end="")
    for j in range (sillas_total):
        if caso_cliente <= sillas_ocupadas:
            print ("    Lugar ocupado por cliente no.", caso_cliente, "   |", end= "")          
            caso_cliente += 1

        else:
            print ("    Silla vacía     |", end= "")

    elegir_opciones ()

def barberia_vacia (): 
    global sillas_ocupadas    
    if sillas_ocupadas == 0:                                                                  
        print ("\nLa barbería está vacía.\nEl barbero está dormido.")

    else:       
        global cola_sillas
        cola_sillas += 1                                                                 
        sillas_ocupadas -= 1

        if sillas_ocupadas > 0:
            print ("\nUn cliente ha salido de la barbería.\nHay sillas disponibles.")

        else:                                                                      
            print ("\nTodos los clientes fueron atendidos.")
            print ("El barbero se durmio.")

    elegir_opciones ()

def elegir_opciones ():
    print("\n\n1. Ver estado de la barbería.")                                          
    print("2. Esperar a ser atendido.")                                              
    print("3. El barbero ha terminado de atender a todos los clientes.")                                           
    print("4. Salir de la barbería\n")

    opciones = int(input("Elija una opción : "))

    if opciones != 4:
        Opcion_cliente (opciones)

elegir_opciones ()