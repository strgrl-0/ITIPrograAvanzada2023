"""
Taller progamacion
-Jugador que más partidas jugo por cada juego
-Jugador que tuvo mejor kda por juego (OMITIDA)
-Juego más jugado
-promedio kda general
-Cantidad partidas jugadas en total
-Por juego mostrar si se ganaron más partidas en clasificatoria o en normal
tomando en consideracion solo las partidas ganadas


(LO DEL KDA ESTA OMITIDO)
Calculo KDA:
    (asesinatos * 0.70 + asistencias * 0.30) / muertes
"""

#Importar numpy
import numpy as np

#Agregar elementos a la lista
def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
 
# Pregunta n1
def mayorJugadorJuegos(filas,columnas,juegosJugadores):
    print("------------------------")
    print("Pregunta 1")
    print("Jugador que más partidas jugo por cada juego:")
    print("------------------------")
    for a in range(columnas):
        mayor = -1
        lista = []
        print("Juego:",juegos[a])
        for b in range(filas):
            lista.append(juegosJugadores[b,a])
            if lista[b] > mayor:
                mayor = lista[b]
                nombreMayor = jugadores[b]
        print("Jugador:",nombreMayor)
        print("Partidas jugadas:",mayor)
        print("------------------------")
 
#Pregunta n2   
def calculoKDA(asesinatos,asistencias,muertes,matriz):
    ase = asesinatos * 0.70
    asi = asistencias * 0.30
    suma = ase + asi
    kda = suma / muertes
    return kda
    
# Pregunta n3
def juegoMayor(filas,columnas,matriz):
    mayor = -1
    lista = []
    for a in range(filas): #Jugadores
        suma = 0
        for b in range(columnas): #Juegos
            suma += matriz[a,b]
        if suma > mayor:
            mayor = suma
            juegoMayor = juegos[b]
    lista = [juegoMayor,mayor]
    return lista
 

#Pregunta n4
def promedioKDA(kills,muertes,asistencias,partidas):
    k = round(kills / partidas,2)
    d = round(muertes / partidas,2)
    a = asistencias / partidas
    promedio = [k,d,a]
    return promedio

  
#Variables
partidasContador = 0 #Pregunta n5
killTotal = 0 #Pregunta n4
asisTotal = 0 #Pregunta n4
muerteTotal = 0 #Pregunta n4
contadorDerrota = 0 #Pregunta n6

#Matrices
juegosJugadores = np.zeros([4,3])
jugadoresPartidas = np.zeros([2,3])

#Listas
juegos = []
resultadoPartidas = []
tipoPartidas = []
jugadores = []
pabloAsesi = []
pabloMuer = []
pabloAsis = []

#Abrir archivo
arch = open("partidas.txt",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    #Dividir en partes
    partes = linea.split(",")
    juego = partes[0]
    resultadoPartida = partes[1]
    kda = partes[2]
    tipoPartida = partes[3]
    jugador = partes[4]
    partesKda = kda.split("/")
    asesinato = int(partesKda[0])
    muerte =  int(partesKda[1]) 
    asis =  int(partesKda[2])    
    
    #Agregar elementos a listas
    agregar(jugadores,jugador)
    agregar(juegos,juego)
    agregar(tipoPartidas,tipoPartida)
    agregar(resultadoPartidas,resultadoPartida)
    
    #Fila y columna
    f = jugadores.index(jugador)
    f1 = tipoPartidas.index(tipoPartida)
    c = juegos.index(juego)
   
    #Contadores
    partidasContador += 1 #Partidas jugadas en total
    killTotal += asesinato #Asesinato totales por todos los jugadores
    asisTotal += asis #Asistencias totales por todos los jugadores
    muerteTotal += muerte #Muertes totales por todos los jugadores
    
    #Agregar cantidad partidas jugadas por jugador
    juegosJugadores[f,c] += 1 #Pregunta n5
    if resultadoPartida == "VICTORIA":
        jugadoresPartidas[f1,c] += 1
    else:
        contadorDerrota += 1
    
    #Lee nueva linea
    linea = arch.readline().strip()

filas = len(jugadores)
filas1 = len(tipoPartidas)
columnas = len(juegos)

#Pregunta n1
print(mayorJugadorJuegos(filas,columnas,juegosJugadores))

#Pregunta n2
"""
Calculo KDA:
    (asesinatos * 0.70 + asistencias * 0.30) / muertes
-Jugador que tuvo mejor kda por juego
"""
# print("Pregunta 2:")
# print("Jugador que tuvo mejor kda por juego:")
 
        
#Pregunta n3
print("------------------------")
print("Pregunta 3:")
print("El juego mas jugado fue:")
n3 = juegoMayor(filas,columnas,juegosJugadores)
print(n3[0],"con",n3[1],"partidas")
print("------------------------")

#Pregunta n4
print("Pregunta 4:")
promedio = promedioKDA(killTotal,muerteTotal,asisTotal,partidasContador)
print("El promedio general del KDA fue:")
print("Kills:",promedio[0])
print("Muertes:",promedio[1])
print("Asistencias:",promedio[2])
print("------------------------")

#Pregunta n5
print("Pregunta 5:")
print("En total se jugaron",partidasContador,"partidas")
print("------------------------")

#Pregunta n6
print("Pregunta 6:")
print("En cada juego se ganaron mas partidas de tipo:")
for a in range(columnas):
    mayor = -1
    for b in range(filas1):
        if jugadoresPartidas[b,a] > mayor:
            mayor = jugadoresPartidas[b,a]
            tipoMayor = tipoPartidas[b]
    print(juegos[a],"Con el tipo de partida",tipoMayor,"con",mayor,"partidas ganadas")
print("En total se perdieron",contadorDerrota,"partidas")

