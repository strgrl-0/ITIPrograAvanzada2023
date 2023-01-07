"""
Libro guia capitulo 9, ej1
#Problema
"""

def calcularPromedio(lista):
    suma = 0
    # "len" retorna cantidad de elementos de la lista
    num = len(lista)
    
    for i in range(0,num):
        suma = suma + lista[i]
        promedio = suma / num
    return promedio

arch = open("numeros.txt","r",encoding = "utf-8")

numeros = []
linea = arch.readline().strip()
while linea != "":
    numero = int(linea)
    numeros.append(numero)
    linea = arch.readline().strip()
    
#Imprimir valores dentro de los limites
prom = calcularPromedio(numeros)
limite1 = prom * 0.8
limite2 = prom * 1.2

#Recorrer lista y el elemento dentro de los limites
c = 0
for x in numeros:
    if x >= limite1 and x <= limite2:
        c = c + 1
        
print(c)