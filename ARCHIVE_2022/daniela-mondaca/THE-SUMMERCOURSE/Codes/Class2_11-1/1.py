taller=[];ii=False
while(len(taller)<5):
    inp=int(input("Ingresa"+'\n'))
    if(inp<0):
        print("No se puede ingresar un valor inferior a 0")
        ii=True
        break
    taller.append(inp)
if(ii==False):
    max=-1
    for i in range(len(taller)):

        for j in range(len(taller)):
            if(taller[i]>max):
                max=taller[j]
    print("El numero mas grande es "+str(max)+'\n')

