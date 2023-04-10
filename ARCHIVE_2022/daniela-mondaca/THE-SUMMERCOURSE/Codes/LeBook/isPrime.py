'''Construya un programa que pregunte un número entero “i” por teclado y escriba por pantalla el i-ésimo número
primo (considere que el primero primo es el 1)'''

readKB=int(input("Ingrese un numero"+'\n'))

#processing
c=0
for i in range(1,9,1):
    isPrimo=readKB%i
    
    if isPrimo==0:
        c+=1
if(c>=3):
    print("numero no primo")
else:
    print("numero primo")
    
    

        
    