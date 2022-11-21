#Class3, Ej1
num=int(input("Ingresa un numero "+'\n'))
numc=str(num)
prim=bool(False)
c=int(len(numc))

#check len
for i in range(c):
    numa=num//2


numb=int(numa*2+1)
if(numb==num):
    print("El numero " + str(num) + " es primo")
if(num==2):
    print("El numero "+str(num)+" es primo")