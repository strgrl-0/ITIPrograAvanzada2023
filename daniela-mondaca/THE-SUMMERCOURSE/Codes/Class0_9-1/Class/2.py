n1=int(input("Ingresa numero 1"+'\n'))
n2=int(input("Ingresa numero 2"+'\n'))

req1=n1%n2

if (n2==0):
    print("No se puede dividir por 0")
    
else:
        
    if (req1!=0):
        print("La division no es entera"+'\n')
        print("El valor del resto es "+str(req1))
    else:
        print("La division es entera")
        
        
    
    #req2
    if (n1==n2):
        print("Los valores son iguales")
        
    elif (n1>n2):
        print("El valor 1 es mayor al valor 2"); print(n2%n1) 
        
        #req3
        if (n1%n2)!=0:
            print("El numero "+str(n1)+" NO es multiplo de "+str(n2))
        else:
            print(str(n1)+" es multiplo de "+str(n2))
            
    elif (n1<n2):
        print("El valor 1 es menor al valor 2"); print(n2%n1) 
                
        #req3
        if (n2%n1)!=0:
            print("El numero "+str(n1)+" NO es multiplo de "+str(n2))
        else:
            print(str(n2)+" es multiplo de "+str(n1))