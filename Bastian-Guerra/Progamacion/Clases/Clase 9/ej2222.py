"""
Clase 9 PPT ejercicios,ej2
"""

import numpy as np

def maximo(lista,mayor,fila,columna):
    mayor = -1
    for i in range(fila):
        for j in range(columna):
            if lista[i] > mayor:
                mayor = lista[i]
    return mayor



#matriz
matriz = np.zeros([6,10])

#Listas
conductores = []
maquinas = []
kilometros = []
usado = []

#Variables
mayor = -1
cont = 0
conductorMayor = "" #Conductor que mas kilometros recorrio
vehiculoMayor = "" #Vehiculo mas usado

#Abrir archivo
arch = open("ej2.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    partes = linea.split(";")
    conductor = partes[0]
    maquina = partes[1]
    kilometro = int(partes[2])
    
    if conductor not in conductores:
        conductores.append(conductor)
    if maquina not in maquinas:
        maquinas.append(maquina)  
        
    f = conductores.index(conductor)
    c = maquinas.index(maquina)
    
    matriz[f][c] = kilometro
    #Leer nueva linea
    linea= arch.readline().strip().lower()
    
fila = len(matriz) #Cantidad de filas en matriz
columna = len(matriz[0]) #Cantidad de columnas

maximo(matriz, mayor, fila, columna)
    