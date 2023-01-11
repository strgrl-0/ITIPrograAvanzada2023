minor=[]; ii=False
while(len(minor)<5):
    inp=int(input("Ingresa"+'\n'))
    if(inp<0):
        print("No se puede calcular el numero menor"); ii=True
        break
    minor.append(inp)

if(ii!=True):
    min=0
    for i in range(len(minor)):
        for j in range(len(minor)):
            if(minor[i]>minor[j]):
                min=minor[j]
    print("El numero menor es "+str(min))