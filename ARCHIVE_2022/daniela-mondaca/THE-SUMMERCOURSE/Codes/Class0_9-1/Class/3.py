fig=input("Ingresa una figura(Triangulo, Circulo o Cubo)"+'\n');pi=3.14

if(fig=="Triangulo"):
    h=int(input("Ingresa la altura"+'\n'));b=int(input("Ingresa la base"+'\n'))
    area=b*h/2
    print("El area es "+str(area))
elif(fig=="triangulo"):
    h=int(input("Ingresa la altura"+'\n'));b=int(input("Ingresa la base"+'\n'))
    area=b*h/2
    print("El area es "+str(area))
if(fig=="Circulo"):
    r=int(input("Ingresa el radio"+'\n'))
    area=pi*r**2
    print("El area es "+str(area))
elif(fig=="circulo"):
    r=int(input("Ingresa el radio"+'\n'))
    area=pi*r**2
    print("El area es "+str(area))
if(fig=="Cubo"):
    l=int(input("Ingresa el lado"+'\n'))
    area=l**2
    print("El area es "+str(area))
elif(fig=="cubo"):
    l=int(input("Ingresa el lado"+'\n'))
    area=l**2
    print("El area es "+str(area))
    
