def imp():
    for i in range(4):
        if (i==0): L=int(input("Ingresa L "'\n')); L=L-1
        elif (i==1): p=int(input("Ingresa p "+'\n')) 
        elif (i==2): q=int(input("Ingresa q "+'\n')) 
        elif (i==3): n=int(input("Ingresa n "+'\n'))
    return(L, p, q, n)

 
L, p, q, n=imp() 


#jmp
for i in range(n):
    print("Juanito se encuentra en la casilla "+str(p))
    print("Avanzara "+str(q)+" casillas")
    strt=p
    p=p+q
    
    print("Juanito avanzo hasta: "+str(p))




