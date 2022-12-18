"""
Ayudantia 11,ej
"""

"""
FALTO HACER 5 , QUE SON LAS 3 AM XD Y TENGO TUTO
"""


import numpy as np

def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

      
#Variables
a = 0
b = 0
mayor = -10**10 #Pregunta numero 2
menor = 10**10 #Pregunta numero 3
contadorReliquia = 0 #Pregunta numero 4
sumaReliquia = 0 #Pregunta numero 4
#Listas
rarezas = []
continentes = []
valores = []
coleccionReliquia = [] #Pregunta numero 4

#Matriz
coleccion = np.zeros([5,5])

#Leer archivo
arch = open("tesoros.txt","r",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    codigo = partes[0]
    rareza = partes[1]
    continente = partes[2]
    valor = float(partes[3])
    
   
    if len(partes) == 5:
        conservar = partes[4]
    else:
        #Agregar elementos lista
        agregar(rarezas, rareza)
        agregar(continentes, continente)
        
        if rareza == "reliquia":
            sumaReliquia += valor
            contadorReliquia += 1
            
        #Filas y columnas
        f = rarezas.index(rareza)
        c = continentes.index(continente)
        
        #Agregar valores a la matriz
        coleccion[f][c] += valor

    
    #Leer nueva linea 
    linea = arch.readline().strip()

fila = len(rarezas)
columna = len(continentes)

#Imprimir la suma total por continente y calculo mayor
print("1) Valor por continente") #Falta ordenar alfabeticamente
for i in range(fila):
    #Resetea la lista mayor y suma para cada columna
    listaMayor = []
    sumaMayor = 0
    print(continentes[i])
    for j in range(columna):
        sumaMayor += coleccion[j,i] 
        listaMayor.append(coleccion[j,i])
    if sumaMayor > mayor:
        mayor = sumaMayor
        coleccionMayor = listaMayor
    print(round(sumaMayor,2),"M")

print("2) Valor por rareza del continente con mayor valor")
for c in range(len(rarezas)):
    print(rarezas[c],round(coleccionMayor[c],2),"M")

#Calculo rareza menor
for i in range(fila):
    listaMenor = []
    sumaMenor = 0
    for j in range(columna):
        sumaMenor += coleccion[i,j]
        listaMenor.append(coleccion[i,j])
    if sumaMenor < menor:
        menor = sumaMenor
        coleccionMenor = listaMenor
        rarezaMenor = i
        
print("3) Coleccion con menor valor")       
print(rarezas[rarezaMenor],menor)

print("4) Valor medio de la coleccion reliquia")
print(round(sumaReliquia / contadorReliquia,2),"M")
