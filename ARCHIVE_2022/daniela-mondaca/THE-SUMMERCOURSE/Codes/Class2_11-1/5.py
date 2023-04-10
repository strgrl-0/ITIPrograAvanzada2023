ii=False;max=-1;NameIndex="default"
for i in range(4):
    inpN=int(input("Ingresa numero"+'\n'))
    if(inpN<0):
        print("No se puede calcular el numero mayor")
        ii=True
        break
    
    inpName=input("Ingresa nombre"+'\n')

    if(max<inpN):
        max=inpN
        NameIndex=inpName

if(ii!=True):
    print(NameIndex+" "+str(max))
    