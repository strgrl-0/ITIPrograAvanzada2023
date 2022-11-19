n1 = int(input("Ingrese un numero"))
n2 = int(input("Ingrese un numero otra vez"))
mOl = str()
multi = int()
nuum = str()

if (n1%n2 == 0):
    print("La division entre ", (n1), " y ", (n2), " es entera")
elif (n1 % n2 != 0):
    print("La división no es entera") 
elif (n2 == 0):
    print("No se puede dividir por 0")
if (n1>n2):
    mOl = str(n1) + " es mayor que " + str(n2)
    multi = (n1%n2)
    nuum = str(n2)+ " es múltiplo de "+ str(n1)
elif (n1<n2):
    mOl = str(n1)+ " es menor que "+ str(n2)
    multi = (n2%n1)
    nuum = str(n1)+ " es multiplo de "+ str(n2)
elif (n1==n2):
    mOl = str(n1)+ " es igual que "+ str(n2)
    multi = (n2%n1)
    nuum = str(n1)+ " es multiplo de "+ str(n2)

print (mOl)
if (multi == 0):
    print(nuum)

