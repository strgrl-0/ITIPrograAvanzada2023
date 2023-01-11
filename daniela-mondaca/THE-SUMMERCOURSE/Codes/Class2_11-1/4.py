prcnt=float(0);elmsP=0;elmsN=0; ii=False
for i in range(6):
    inp=float(input("Ingresa"+'\n'))
    if(inp<0):
        print("No se puede realizar el calculo"); ii=True
        break
    
    if(inp>=3.96):
        elmsP+=1
        elmsN+=1
    else:
        elmsN+=1
        
if(ii!=True):
    prcnt=100*elmsP/elmsN

    print("El porcentaje de notas sobre 4.0 es "+str(prcnt))