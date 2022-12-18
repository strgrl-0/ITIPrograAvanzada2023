"""
Ayudantia 11
"""
import numpy as np

#Agregar elementos listas
def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

#Ordenar listas
def ordenar(lista1,lista2):
    for a in range(len(lista1) - 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] < lista1[b]:
                intecambiar(lista1,a,b)
                intecambiar(lista2,a,b)

#Intercambias valores
def intecambiar(lista,indice1,indice2):     
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux

#Pregunta 1 y 2
def valorContinente(filas,columnas):
    for a in range(filas):
        suma = 0
        print(continentes[a])
        for b in range(columnas):
            suma += valores[b,a]
        print(round(suma,2),"M")
        

#Matrices
valores = np.zeros([5,5])

#Listas
rarezas = []
continentes = []


arch = open("tesoros.txt",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    codigo = partes[0]
    rareza = partes[1]
    continente = partes[2]
    valor = float(partes[3])
    
    if len(partes) > 4:
        conservar = partes[4]
    else:
        #Agregar elementos listas
        agregar(rarezas,rareza)
        agregar(continentes,continente)

        f = rarezas.index(rareza)
        c = continentes.index(continente)
        
        valores[f,c] += valor
    
    #Leer nueva linea
    linea = arch.readline().strip()

filas = len(rarezas)
columnas = len(continentes)

#Pregunta 1
print("1) Valor por continente")
print(valorContinente(filas,columnas))
  
#Pregunta 2
mayor = -1
continenteMayor = 0
sumaContinente = 0
valorRareza = 0
sumaRareza = 0
print("2) Valor por rareza del continente con mayor valor")     
