"""
Clase 7 ejercicios PPT, ej4
Cree una función que tome una lista con números y calcule:
-El mínimo
-El máximo
-El promedio
-La suma
Pruebe su solución leyendo el archivo que ve en la imagen de al lado.
"""

def minimo(lista,menor):
    menor = 10**10
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def maximo(lista,maximo):
    maximo = -100000
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def promedio(lista):
    suma = 0
    c = 0
    for i in range(len(lista)):
        suma += lista[i]
        c += 1
    prom = suma / c
    return prom

def total(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

mayor = -100000
menor = 10**10
lista = []

arch = open("numeros.txt","r",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    lista.append(int(linea))
    linea = arch.readline().strip()
    
numero_menor = minimo(lista,menor)
numero_mayor = maximo(lista,mayor)
numero_promedio = promedio(lista)
suma = total(lista)
print("Lista original:",lista)
print("El numero menor de la lista es:",numero_menor)
print("El numero mayor de la lista es:",numero_mayor)
print("El numero promedio de la lista es:",numero_promedio,"(",suma,"/",len(lista),")")
print("La suma total de la lista es:",suma)