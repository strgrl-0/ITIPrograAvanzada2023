fig=str(input("Ingrese una figura" '\n'))
target=int(0)
print(fig)

if(fig) in  ['triangulo', 'Triangulo']:
    target=1
    print(target)
elif(fig) in ['circulo', 'Circulo']:
    target=2
    print(target)
elif(fig) in ['cubo', 'Cubo']:
    target=3
    print(target)
    
###########################################

if(target==1):
    trgH=float(input("Altura del triangulo" '\n'))
    trgB=float(input("Base del triangulo" '\n'))

    rt = trgH*trgB/2
    print("El area del triangulo es "+str(rt)+" unidades cuadradas")

elif(target==2):
    cirR=float(input("Radio del circulo" '\n'))

    rc = 3.14*cirR**2
    print("El Area del circulo es "+str(rc)+" unidades cuadradas")

elif(target==3):
    cuS=float(input("Lado del cubo" '\n'))

    rcu=cuS**2*6
    print("El Area del cubo es "+str(rcu)+" unidades cuadradas")
