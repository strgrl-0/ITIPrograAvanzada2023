"""
Bastian Guerra Valdés, ITI , Ejercicio 2,clase 3
"""
n1 = int(input("Ingrese el número inicial: "))
n2 = int(input("Ingrese el número final: "))
suma = 0

for i in range(n1 + 1,n2):
    suma += i
    print(suma)

n3 = int(input("Ingrese el tercer valor: "))

for i in range(n1,n2 + 1,n3):
    print(i)