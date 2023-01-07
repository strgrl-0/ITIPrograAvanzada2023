"""
Simulacro prueba 2,Bastian guerra,ej1
"""
import numpy as np


def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)


#Matriz
bodega = np.zeros([6,6])
despachados = np.zeros([6,6])

#Variables
costoTotal = 0 #Pregunta numero 3
cantDespachos = 0 #Pregunta numero 3
mayor = -1 #Pregunta numero 4
zonaMayor = 0 #Pregunta numero 4
sectorMayor = 0 #Pregunta numero 4


#Listas
fechas = []
items = []
zonaSectores = []
zonas = ["A","B","C","D","E","F"]
sectores = [1,2,3,4,5,6]
precios = [125,325,198,635,312,185]

#Abrir archivo
arch = open("recibidos.txt","r",encoding = "utf-8")
linea = arch.readline().strip().upper()

while linea != "":
    #Dividir partes
    partes = linea.split(";")
    fecha = partes[0]
    zonaSector = partes[1]
    item = int(partes[2])
    
    zs = zonaSector.split("-")
    zona = zs[0]
    sector = int(zs[1])
    
    #Agregar lista
    agregar(fechas,fecha)
    agregar(zonaSectores,zonaSector)
    agregar(items,item)
    
    f = zonas.index(zona)
    c = sectores.index(sector)

    if bodega[f][c] + item >= 100:
        bodega[f][c] =  bodega[f][c] + item - 100
        despachados[f][c] += 1
        print("Se realiza despacho en",zona,sector,"el",fecha)
        
        if sector == 1:
            costoTotal += 125
            cantDespachos += 1
        elif sector == 2:
            costoTotal += 325
            cantDespachos += 1
        elif sector == 3:
            costoTotal += 198
            cantDespachos += 1
        elif sector == 4:
            costoTotal += 635   
            cantDespachos += 1
        elif sector == 5:
            costoTotal += 312  
            cantDespachos += 1
        elif sector == 6:
            costoTotal += 185
            cantDespachos += 1
    else:
        bodega[f,c] += item
    
    
    #Leer nueva linea
    linea = arch.readline().strip().upper()

filas = len(zonas)
columnas = len(sectores)

#Pregunta numero 4
for i in range(filas):
    pendientes = 0
    for j in range(columnas):
        if bodega[i,j] > mayor:
            mayor = bodega[i,j]
            sectorMayor = sectores[j]
            zonaMayor = zonas[i]
    

#Imrpimir resultador
print("2) Los envios por zona-sector en el mes fueron:")
print(despachados)
print("3) El costo total de los",costoTotal,"despachos fue de",costoTotal)
print("4) Las ubicaciones con la mayor cantidad de items pendientes son:")
print(zonaMayor,"-",sectorMayor,"con",mayor)
print("5) el total de items pendientes por zonas:")
#Pregunta numero 5
for i in range(filas):
    pendientes = 0
    for j in range(columnas):
        pendientes += bodega[i,j] #Pregunta numero 5
        pendientesZona = zonas[i] #Pregunta numero 5
    print("Zona",pendientesZona,pendientes)
