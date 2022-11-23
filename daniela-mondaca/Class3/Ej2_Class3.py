


def imp():
    for i in range(4):
        if (i==0): L=int(input("Ingresa L "'\n')); L=L-1
        if (L>1): keep=False; 
        if(L<2): print("El tamaño del mundo no puede ser uno o menor")
        elif (i==1): p=int(input("Ingresa p "+'\n')) 
        elif (i==2): q=int(input("Ingresa q "+'\n')) 
        elif (i==3): n=int(input("Ingresa n "+'\n'))
    return(L, p, q, n, keep)

keep=True
while(keep==True):  
    L, p, q, n, keep=imp() 

#wrldif
def wdif(p1,L1):
    

    return(p1)


#jmp
for i in range(n):
    print("Juanito se encuentra en la casilla "+str(p))
    print("Avanzara "+str(q)+" casillas")
    p=p+q
    if(p>L):
        dif=int(p-L)
        p=p-dif
    print("Juanito avanzo hasta: "+str(p))




