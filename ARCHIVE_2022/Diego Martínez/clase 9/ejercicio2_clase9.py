# Diego Marti­nez
# ejercicio 2, clase 9

def imprimir(lista1,lista2):
    indice = lista1.index(max(lista1))
    print('\n->',lista2[indice])

def imprimir_1(lista1,lista2):
    indice = lista1.index(max(lista1))
    print('\n->',lista2[indice].lower())

import numpy as np
        
trabajo = np.zeros([100,100])
nombres = []
maquinas = []
usadas = []
distancias = []
cont = 0
suma = 0

arch = open('ejercicio.txt')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(';')
    nombre = partes[0].upper()
    maquina = partes[1]
    distancia = int(partes[2])

    if nombre not in nombres:
        nombres.append(nombre)
    if maquina not in maquinas:
        maquinas.append(maquina)
    
    f = nombres.index(nombre)
    c = maquinas.index(maquina)
    
    trabajo[f][c] = distancia  
    linea = arch.readline().strip()

fila = len(trabajo)
columna = len(trabajo[0])

for i in range(columna):
    if i != 0:
        usadas.append(cont)
    cont = 0
    if i == len(maquinas):
        break
    for x in range(fila):
        if trabajo[x][i].any():
            cont += 1
        else:
            continue

for i in range(fila):
    if i != 0:
        distancias.append(suma)
    if i == len(nombres):
        break
    suma = 0
    for x in range(columna):
        if trabajo[i][x].any():
            suma += trabajo[i][x]
        else:
            continue

imprimir_1(distancias,nombres)
imprimir(usadas,maquinas)

