# Diego Martínez
# Ejercicio 1, Ayudantia 10

import numpy as np

def crearmatriz(a):
    
    def porcentaje(a):
        total = a *100
        return total
    
    arch = open(a)  
    linea = arch.readline().strip()
    partes = linea.split(',')
    fil = int(partes[0])
    col = int(partes[1])
    matriz = np.zeros([fil,col])
    linea = arch.readline().strip()
    f = 0
    
    while  linea != '':
        
        partes = linea.split(',')
        c = int(partes[0])
        for a in range(len(partes)):
            for b in range(c):
                por = porcentaje(float(partes[b+1]))                
                matriz[f][b] = por
        f += 1
        linea = arch.readline().strip() 
    return matriz

def territorio(matriz):
    fila = matriz.shape[0]
    columna = matriz.shape[1]
    cont = 0
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j] >= 65.0:
                cont += 1
            else:
                continue
    cuadrantes = cont*21
    return cuadrantes

def orden(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux

def conseguir(matriz,posición,valores):
    fila = matriz.shape[0]
    columna = matriz.shape[1]
    for i in range(fila):
        for j in range(columna):
            valores.append(matriz[i][j])
            posición.append([i,j])
    return matriz

def nulos(matriz):
    fila = matriz.shape[0]
    columna = matriz.shape[1]
    cont = 0
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j].any():
                continue
            else:
                cont += 1
    return cont

def nonulos(matriz):
    fila = matriz.shape[0]
    columna = matriz.shape[1]
    cont = 0
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j].any():
                cont += 1
            else:
                continue
    return cont

def nonulos_sum(matriz):
    fila = matriz.shape[0]
    columna = matriz.shape[1]
    suma = 0
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j].any():
                suma += matriz[i][j]
            else:
                continue
    return suma

def imprimir(lista,lista2,a,b,c):
    print('\n1. Coordenadas de los cinco cuadrantes con mayor probabilidad:')
    for i in range(5):
        print('\t> El cuadrante',lista2[i],'tiene una probabilidad del',lista[i],'%')
    print('\n2. La probabilidad promedio de encontrar la especie en cuadrantes no nulos es:',round(a,2),'%')
    print('\n3. La cantidad de cuadrantes nulos es:',b)
    print('\n4. El area total de cuadrantes con probabilidad alta (>=65%) es: (',c,') [km**2]')

leer = 'diversidad_costera.txt'
matriz = crearmatriz(leer)

posiciones = []
valores = []

fila = matriz.shape[0]
columna = matriz.shape[1]

total_casillas = fila * columna
conseguir(matriz,posiciones,valores)

# Primera pregunta ->
for a in range(len(valores)-1):
    for b in range(a+1,len(valores)):
        if valores[a]<valores[b]:
            orden(valores,a,b)
            orden(posiciones,a,b)
        elif valores[a] == valores[b]:
            if valores[a]<valores[b]:
                orden(valores,a,b)
                orden(posiciones,a,b)

# tercera pregunta ->
casillas_nulas = nulos(matriz) # Respuesta 3ra pregunta

# Segunga respuesta ->
casillas_nonulas = nonulos(matriz)
total_nonulas = nonulos_sum(matriz)
promedio = total_nonulas/casillas_nonulas # Respuesta 2da pregunta

# Cuarta pregunta ->
probabilidad_cuadrantes = territorio(matriz) # Respuesta 4ta pregunta

imprimir(valores,posiciones,promedio,casillas_nulas,probabilidad_cuadrantes)
