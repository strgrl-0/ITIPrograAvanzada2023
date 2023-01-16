inpName="default";inpNum=float(0);LowestHNumc=float(0);HighestLNumc=float(0);LowestHName="def";HighestLName="def";keep=True;show=bool(False)
calc=bool(True);Total=0;Max=-1;Min=7.1;prcntH=0;prcntL=0

while(keep==True):
    inpName=input("Ingresa nombre"+'\n')
    
    if(inpName=="FIN" or inpName=="fin" or inpName=="Fin"):

        if(inpNum==0.0):
            print("No se ha ingresado nada, saliendo")
            break
        show=True
        if(show==True):
            prcntH=100*LowestHNumc/Total;prcntL=100*HighestLNumc/Total
            print("Total de notas ingresadas validas: "+str(Total)+'\n')
            print("Cantidad de notas mayores o iguales a 4.0: "+str(LowestHNumc)+' '+"("+str(prcntH)+"%)")
            print("La menor fue: "+str(Min)+' '+LowestHName)
            print("Cantidad de notas menores a 4.0: "+str(HighestLNumc)+' '+"("+str(prcntL)+"%)")
            print("La mayor fue: "+str(Max)+' '+HighestLName)
        break
    
    inpNum=float(input("Ingresa nota"+'\n'))
    
    if(inpNum)<0:
        print("La nota no puede ser menor a 0")
        calc=False
    if(calc==True):
        if(inpNum>=3.96):
            Total+=1;LowestHNumc+=1
            if(inpNum<Min):
                Min=inpNum
                LowestHName=inpName
        elif(inpNum<=3.95):
            Total+=1;HighestLNumc+=1
            if(inpNum>Max):
                Max=inpNum
                HighestLName=inpName
        