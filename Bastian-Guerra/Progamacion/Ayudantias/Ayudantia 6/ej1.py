"""
Ayudantia 6,ej1
#Problema:
Cree un programa que solicite 10 números por pantalla y calcule el mayor y el menor
de estos números utilizando funciones
"""

#Funciones
def ingresar(numero):
    numero = float(input("Ingrese numero: "))
    return numero

def numeracion(numero):
    x = print("Usted va a ingresar el numero:",numero)
    return x
    
def mayor(mayorn,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6 and n1 > n7 and n1 > n8 and n1 > n9 and n1 > n10:
        mayor = n1
        return mayor
    if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6 and n2 > n7 and n2 > n8 and n2 > n9 and n2 > n10:
        mayor = n2
        return mayor
    if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5 and n3 > n6 and n3 > n7 and n3 > n8 and n3 > n9 and n3 > n10:
        mayor = n3    
        return mayor
    if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5 and n4 > n6 and n4 > n7 and n4 > n8 and n4 > n9 and n4 > n10:
        mayor = n4
        return mayor
    if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4 and n5 > n6 and n5 > n7 and n5 > n8 and n5 > n9 and n5 > n10:
        mayor = n5
        return mayor
    if n6 > n1 and n6 > n2 and n6 > n3 and n6 > n4 and n6 > n5 and n6 > n7 and n6 > n8 and n6 > n9 and n6 > n10:
        mayor = n6
        return mayor
    if n7 > n1 and n7 > n2 and n7 > n3 and n7 > n4 and n7 > n5 and n7 > n6 and n7 > n8 and n7 > n9 and n7 > n10:
        mayor = n7
        return mayor
    if n8 > n1 and n8 > n2 and n8 > n3 and n8 > n4 and n8 > n5 and n8 > n6 and n8 > n7 and n8 > n9 and n8 > n10:
        mayor = n8
        return mayor
    if n9 > n1 and n9 > n2 and n9 > n3 and n9 > n4 and n9 > n5 and n9 > n6 and n9 > n7 and n9 > n8 and n9 > n10:
        mayor = n9
        return mayor
    if n10 > n1 and n10 > n2 and n10 > n3 and n10 > n4 and n10 > n5 and n10 > n6 and n10 > n7 and n10 > n8 and n10 > n9:
        mayor = n10
        return mayor
 
def menor(menorn,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5 and n1 < n6 and n1 < n7 and n1 < n8 and n1 < n9 and n1 < n10:
        menor = n1
        return menor
    if n2 < n1 and n2 < n3 and n2 < n4 and n2 <n5 and n2 < n6 and n2 < n7 and n2 < n8 and n2< n9 and n2 < n10:
        menor = n2
        return menor
    if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5 and n3 < n6 and n3 < n7 and n3 < n8 and n3 < n9 and n3 < n10:
        menor = n3    
        return menor
    if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5 and n4 < n6 and n4 < n7 and n4 < n8 and n4 < n9 and n4 < n10:
        menor = n4
        return menor
    if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4 and n5 < n6 and n5 < n7 and n5 < n8 and n5 < n9 and n5< n10:
       menor = n5
       return menor
    if n6 < n1 and n6 < n2 and n6< n3 and n6< n4 and n6 <n5 and n6 < n7 and n6< n8 and n6< n9 and n6< n10:
        menor = n6
        return menor
    if n7 < n1 and n7 < n2 and n7 < n3 and n7 < n4 and n7 < n5 and n7 < n6 and n7 < n8 and n7 < n9 and n7< n10:
        menor = n7
        return menor
    if n8 < n1 and n8 < n2 and n8 < n3 and n8 < n4 and n8 < n5 and n8 < n6 and n8 < n7 and n8 < n9 and n8< n10:
        menor = n8
        return menor
    if n9 < n1 and n9 < n2 and n9 < n3 and n9 < n4 and n9 < n5 and n9 < n6 and n9 < n7 and n9 < n8 and n9 < n10:
        menor = n9
        return menor
    if n10 < n1 and n10 < n2 and n10 < n3 and n10 < n4 and n10 < n5 and n10< n6 and n10 < n7 and n10 < n8 and n10< n9:
        menor = n10
        return menor
       
"Progama"
#Variables
mayorn = -10*10
menorn = 10*10
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0

numeracion(1)
n1 = ingresar(n1)
numeracion(2)
n2 = ingresar(n1)
numeracion(3)
n3 = ingresar(n1)
numeracion(4)
n4 = ingresar(n1)
numeracion(5)
n5 = ingresar(n1)
numeracion(6)
n6 = ingresar(n1)
numeracion(7)
n7 = ingresar(n1)
numeracion(8)
n8 = ingresar(n1)
numeracion(9)
n9 = ingresar(n1)
numeracion(10)
n10 = ingresar(n1)
numeroMayor = mayor(mayorn,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
numeroMenor = menor(menorn,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
print("El numero mayor de los numeros ingresados es:",numeroMayor)
print("El numero menor de los numeros ingresados es:",numeroMenor)

