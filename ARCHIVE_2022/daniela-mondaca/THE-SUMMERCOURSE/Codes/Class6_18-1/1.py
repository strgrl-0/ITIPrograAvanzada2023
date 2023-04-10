keep=True; checkCant=True; checkType=True

def ventas(cantidad,tipo):
    tipoValor=0
    
    if(tipo=='CANCHA'):
        tipoValor=20000
    elif(tipo=='PLATEA'):
        tipoValor=30000
    elif(tipo=='TIPO'):
        tipoValor=40000
        
    a_cancelar=int(cantidad*tipoValor)
    return(a_cancelar)

while(keep==True):

    if(checkType==True):
        cantidad=int(input("Ingrese la cantidad de entradas"+'\n'))
        if(cantidad<=0):
            print("No se pueden comprar 0 entradas")
            checkCant==False
        else:
            checkCant==True
    if(checkCant==True):
        tipo=str(input("Ingrese el tipo de entradas"+'\n').upper()+'\n')
        print(tipo)#deb
        if(tipo!='CANCHA''SALIR'):  #repair
            print("Ingrese un tipo valido")
            checkType=False
        else:
            checkType=True
    if(checkType==True and checkCant==True):
        salePrice=ventas(cantidad,tipo)
        print("El precio a cancelar es "+str(salePrice))
    
    if(tipo=='SALIR'):
        keep=False