#Sim EJ1 - Eclipse

#Declare vars
llamadosDCurrent=int(0);NombreCliente=str("def");DiasReserva=int(0)
Tarifa=str("def");Confirmacion=str("def");DiasADI=int(-1)

#checkers
chckLlamados=bool(True);chckNombre=bool(True);chckDias=bool(True);chckTar=bool(True);chckCONF=bool(True)
keepDiasAd=bool(True);exec=bool(True)
#No se puede llamar menos que 0 (no llamar a nadie)
llamadosDCurrent=int(input("Ingrese los llamados diarios que se harán hoy"+'\n'))

while(chckLlamados==True):
    if(llamadosDCurrent<0):
        print("No se pueden ingresar numeros negativos") #errCTL
        llamadosDCurrent=0
    elif(llamadosDCurrent==0):
        print("Hoy no se ha llamado a nadie")
        chckLlamados==False;exec=False;break
    else:
        chckLlamados==False;break
        
        
#Counts

ReservasConfDia=int(0);ReservasTotalesDia=int(0);MasConf=int(0);MostConfClient=str("def");IngresosDia=int(0);IngresosDiasExtra=int(0)
FreedUP=int(0);toPay=int(0);Devo=float(0);ReservedP=int(0);ReservedS=int(0)
        
if(exec==True):
    for i in range(llamadosDCurrent):
        #reset vars
        llamadosDCurrent=int(0);NombreCliente=str("def");DiasReserva=int(0)
        Tarifa=str("def");Confirmacion=str("def");DiasADI=int(-1)
        
        #the torture starts
        while(chckNombre==True):
            NombreCliente=str(input("Ingrese nombre del cliente"+'\n'))
            if(NombreCliente==""):
                print("El nombre no se puede dejar en blanco")
            else:
                chckNombre==False
                break     
        
        while(chckDias==True):
            DiasReserva=int(input("Dias reservados: ")+'\n')
            if(DiasReserva<=0):
                print("Se debe reservar al menos un dia")
            else:
                chckDias==False
                break
            
        while(chckTar==True):
            Tarifa=str(input("Ingrese la tarifa"+'\n').upper())
            if(Tarifa!="S" and Tarifa!="P"):
                print("Ingrese una opcion valida")
            else:
                chckTar==False
                break
            
        while(chckCONF==True):
            Confirmacion=str(input("Confirma reserva?(S/N)"+'\n').upper())
            if(Confirmacion!="S" and Confirmacion!="N"):
                print("Ingrese una opcion valida")
            else:
                chckCONF==False
                break

            
        #req1    
        if(Confirmacion=="S"):
            ReservasConfDia+=1;ReservasTotalesDia+=1
            
        elif(Confirmacion=="N"):
            ReservasTotalesDia+=1
            
            

        if(Confirmacion=="S"):
            while(keepDiasAd==True):  
                DiasADI=int(input("Desea agregar dias adicionales?(Ingrese 0 si no agrega)"+'\n'))   
                        
                if(DiasADI<0):
                    print("No se pueden ingresar numeros negativos")
                #Calc toPay
                    
                if(DiasADI>=0):


                    if(Tarifa=="S"):
                        toPay=(DiasReserva+DiasADI)*120


                    elif(Tarifa=="P"):
                        toPay=(DiasReserva+DiasADI)*250
                        

                    print("Monto total a pagar: USD "+str(toPay))
                    break

        elif(Confirmacion=="N"):
            if(Tarifa=="S"):
                Devo=DiasReserva*120*0.75
            elif(Tarifa=="P"):
                Devo=DiasReserva*250*0.75
                
            print("Reserva cancelada, devolución: USD "+str(Devo))
        
        #req2-3-4-5
        if(Confirmacion=="S"):
            DiasConf=0
            DiasConf=DiasReserva+DiasADI
            
 
            if(DiasConf>MasConf):
                MasConf=DiasConf
                MostConfClient=NombreCliente
    
        #Dollar calculations
        #conv---------dollar=680CLP
        PrecioReserva=int(0);PrecioAdicionales=int(0);PrecioReservaTot=int(0)
        if(Tarifa=="S"):
            PrecioReserva=(DiasReserva*120)*680
            #Dias Adicionales
            PrecioAdicionales=(DiasADI*120)*680
            PrecioReservaTot=PrecioReserva+PrecioAdicionales
            
        elif(Tarifa=="P"):
            PrecioReserva=(DiasReserva*250)*680
            #Dias Adicionales
            PrecioAdicionales=(DiasADI*250)*680
            PrecioReservaTot=PrecioReserva+PrecioAdicionales
        
        #Calc 25% de cancelacion 
        if(Confirmacion=="N"):
            PrecioCancelacion=int(0)
            PrecioCancelacion=PrecioReserva*0.25
            IngresosDia+=PrecioCancelacion
            FreedUP+=PrecioReserva
            
            if(Tarifa=="S"):
                ReservedS=ReservedS-DiasReserva
            elif(Tarifa=="P"):
                ReservedP=ReservedP-DiasReserva
            
        elif(Confirmacion=="S"):
            IngresosDia+=PrecioReservaTot
            IngresosDiasExtra+=PrecioAdicionales
            
            if(Tarifa=="S"):
                ReservedS+=DiasReserva+DiasADI
            elif(Tarifa=="P"):
                ReservedP+=DiasReserva+DiasADI
                
               
            
            
        
        
    
    #Output
    print("-----------------------------"+'\n')
    #req1-procOut
    prcnt=float(0.0);prcnt=ReservasConfDia*100/ReservasTotalesDia
    print("Hoy se ha confirmado "+str(ReservasConfDia)+" cliente(s) ("+str(prcnt)+"%)")
    #req2-Out
    print("El cliente confirmado que más dias reservó fue: "+MostConfClient)
    #req3-Out
    print("El ingreso confirmado para hoy es: CLP "+str(IngresosDia))
    #req4-Out
    print("El ingreso por dias extra agregados es de: CLP "+str(IngresosDiasExtra))
    #req5-Out
    print("El posible ingreso por habitaciones libres es: CLP "+str(FreedUP))
    #req6-Out
    print("Habitaciones reservadas: "+str(ReservedS)+" Standard, "+str(ReservedP)+" Premium")
    #debug
    