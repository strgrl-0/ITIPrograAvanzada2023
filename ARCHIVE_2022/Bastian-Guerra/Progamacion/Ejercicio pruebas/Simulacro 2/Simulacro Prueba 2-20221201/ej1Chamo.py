# Diego Martìnez 
# Ejercicio 1, Simulacro

def imprimir_2da(a):
    print('\n2) Los envios por zona-sector en el mes fueron:')
    print(a)
    
def imprimir_3ra(a,b):
    print('\n3) El costo total de los',a,'despachos es',b)

def imprimir_4ta(a,b,c):
    print('\n4) Las ubicaciones con la mayor cantidad de items pendientes son:')
    print('\t->',a,'-',b,c)
    
def orden(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
def mayoramenor(a,b):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] < a[j]:
                orden(b,i,j)
                orden(a,i,j)
            elif a[i] == a[j]:
                if a[i] < a[j]:
                    orden(b,i,j)
                    orden(a,i,j)
                    
def imprimir_5ta(lista1,lista2):
    print('\n5) El total  de items pendientes por zonas:')
    for i in range(len(lista1)):
        print('-> Zona',lista1[i],'-',lista2[i])
    
import numpy as np

sectores = ['A','B','C','D','E','F']
zonas = [1,2,3,4,5,6]
despachos_sector = []
filas = len(sectores)
columnas = len(zonas)
total_pagar = 0
cont = 0
mayor = -1
mayor_sector = ''
mayor_zona = 0
suma = 0

zonas_sectores = np.zeros([filas,columnas])
despachados = np.zeros([filas,columnas])

arch = open('recibidos.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(';')
    fecha = partes[0]
   
    duo = partes[1]
    item = int(partes[2])
    partes = duo.split('-')
    sector = partes[0]
    zona = int(partes[1])
    
    f = sectores.index(sector)
    c = zonas.index(zona)
    
    zonas_sectores[f][c] += item
    if zonas_sectores[f][c] >= 100:
        cont += 1
        
        if zonas[c] == 1:
            total_pagar += 125
        elif zonas[c] == 2:
            total_pagar += 325
        elif zonas[c] == 3:
            total_pagar += 198
        elif zonas[c] == 4:
            total_pagar += 635
        elif zonas[c] == 5:
            total_pagar += 312
        elif zonas[c] == 6:
            total_pagar += 185
        
        resta = zonas_sectores[f][c] - 100
        zonas_sectores[f][c] = resta
        print('Se realiza un despacho en',sectores[f],zonas[c],'el',fecha)
        despachados[f][c] += 1 

    linea = arch.readline().strip()

for i in range(filas):
    for j in range(columnas):
        if mayor < zonas_sectores[i][j]:
            mayor = zonas_sectores[i][j]
            mayor_sector = sectores[i]
            mayor_zona = zonas[j]
            
for i in range(filas+1):
    if i != 0:
        despachos_sector.append(suma)
    if i == filas:
        break
    suma = 0
    for j in range(columnas):
        suma += zonas_sectores[i][j]
        
mayoramenor(despachos_sector,sectores)

imprimir_2da(despachados)
imprimir_3ra(cont,total_pagar)
imprimir_4ta(mayor_sector,mayor_zona,mayor)
imprimir_5ta(sectores,despachos_sector)

