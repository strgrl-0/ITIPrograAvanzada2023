# Diego Martinez C7
# 1er ejercicio 

#---------------------FUNCIONES---------------------

def jugador_dadasvuelta(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)
    maxi = -111
    max_jugador = ''
    max_juego = ''
    
    for i in range(f):
        for j in range(c):
            if maxi < mtx[i][j]:
                maxi = int(mtx[i][j])
                max_jugador = lista1[i]
                max_juego = lista2[j]
                
    print('\nPregunta 1')
    print(max_jugador,'terminó',maxi,'el juego',max_juego)
    
def juego_masjuegado(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)
    suma = 0
    maxi = -111
    lista = []
    
    for i in range(f+1):
        if i != 0:
            lista.append(suma)
        if i == f:
            break
        suma = 0
        for j in range(c):
            suma += mtx[i][j]
    
    for i in lista:
        if maxi < i:
            maxi = i
            
    indice = lista.index(maxi)
    print('\nPregunta 2')
    print('El o los juegos mas jugados fueron:')
    print('\t',lista2[indice])
    
def jugadores_juegos(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)
    
    print('\nPregunta 3')
    
    for i in range(f): 
        lista = []
        for j in range(c):             
            lista.append(mtx[i][j])
                
        print(lista1[i],'jugó los titulos:')
        for i in range(len(lista)):
            if lista[i] == 0:
                continue
            print('\t',lista2[i],'y lo terminó en',lista[i])
            
def jugadores_juegos_promedio(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)
    lista = []
    
    print('\nPregunta 4')
    
    print('tiempo promedio gastado jugando:')
    for i in range(f):
        lista = []
        suma = 0
        for j in range(c):
            if mtx[i][j] != 0:
                lista.append(mtx[i][j])
            else:
                continue
        for x in lista:
            suma += x
        print('\t',lista1[i],':',round(suma/len(lista),2),'horas')
        
def records(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)
    
    print('\nPregunta 5')
    
    for i in range(c):
        mini = 99999
        lista = []
        for j in range(f):
            lista.append(mtx[j][i])
            
        for x in lista:
            if mini > x and x != 0:
                mini = x
        indice = lista.index(mini)
        
        print(lista2[i],'fue terminadado en un tiempo record de',mini,'horas por:')
        print('\t-',lista1[indice])
        
def porcentaje(a,b):
    total = (a*100)/b
    return round(total,2)
        
def porcentajes_total(mtx,lista1,lista2):
    f = len(lista1)
    c = len(lista2)    
    total = 0
    
    print('\nPregunta 6')
    print('Porcentahes de teimpos jugados:')
    
    for i in range(f):
        for j in range(c):
            total += mtx[i][j]
            
    for i in range(f):
        suma = 0
        for j in range(c):
            suma += mtx[i][j]
            
        print('\t',lista1[i],'tuvo un porcentaje de',porcentaje(suma,total))

#---------------------LISTAS/FUNCIONES/MATRICES---------------------      
          
import numpy as np

nombres = []
juegos = []
minimos = []
mini = 99999
total = 0

gg = np.zeros([10,10])
dadas_vuelta = np.zeros([10,10])
juegos_menoshoras = np.zeros([10,10])

arch = open('juegos_amistad.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

#---------------------PROGRAMA---------------------

while linea != '':
    
    partes = linea.split(',')
    nombre = partes[0].upper()
    juego = partes[1].upper()
    horas_jugadas = int(partes[2])
    
    if nombre not in nombres:
        nombres.append(nombre)
    if juego not in juegos:
        juegos.append(juego)
        
    f = nombres.index(nombre)
    c = juegos.index(juego)
    
    gg[f][c] += horas_jugadas
    dadas_vuelta[f][c] += 1
    
    juegos_menoshoras[f][c] = horas_jugadas
    
    if mini >juegos_menoshoras[f][c]:
        mini = juegos_menoshoras[f][c]
        juegos_menoshoras[f][c] = mini
    
    
    linea = arch.readline().strip()
  
#---------------------SALIDA---------------------  
  
jugador_dadasvuelta(dadas_vuelta,nombres,juegos)
juego_masjuegado(dadas_vuelta,nombres,juegos)
jugadores_juegos(juegos_menoshoras,nombres,juegos)
jugadores_juegos_promedio(gg,nombres,juegos)
records(juegos_menoshoras,nombres,juegos)
porcentajes_total(dadas_vuelta,nombres,juegos)
