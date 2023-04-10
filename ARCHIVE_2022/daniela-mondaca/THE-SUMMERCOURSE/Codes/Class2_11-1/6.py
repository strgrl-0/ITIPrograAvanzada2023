keep=True;inpName="default";inpNum=-1;conf=0;n="def";Max=0
while(keep==True):
    inpName=input("Ingresa Nombre"+'\n')
    if(inpName=="Cerrar" or inpName=="cerrar"):
        conf=int(input("Confirmacion (1 para si, cualquier numero para no)"+'\n'))
    if(conf==1):
        if(n=="def" and Max==0):
            break
        print(str(n)+' '+str(Max))
        break
    inpNum=int(input("Ingresa Numero"+'\n'))
    if(inpNum<-1):
        print("No se puede ingresar numeros menores a 0")
        break
    elif(inpName=="default" or inpNum==-1):
        print("No se pueden ingresar valores vacios")
        break

    if(Max<=inpNum):
        Max=inpNum
        n=inpName
        
        
    
