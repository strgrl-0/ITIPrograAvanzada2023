
fechas = []
zonas_sectores = []
cant = []
zonas = ['A','B','C','D','E','F']
sectores = [1,2,3,4,5,6]
precios = [125,325,198,635,312,185]
despachos_sector = []

costo_total = 0
cant_despachos = 0
ifila = 0
jcolumna = 0
mayorA = 0
suma = 0
i = 0


import numpy as np
matriz1 = np.zeros([6,6]) #matriz1 es para la bodega#
matriz2 = np.zeros([6,6]) #matriz2 es para los despachos#
vector = np.zeros([1,2]) #retorno posición mayor cantidad de elementos pendientes#
m_suma = np.zeros([6,1])

def agregar_dato(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)       

def mayor_pendientes(matriz):
    global ifila
    global jcolumna
    global mayorA 
    mayor = matriz1[0][0]
    vector = [0,0]
    for i in range (6):
        for j in range (6):
            if matriz1[i][j] > mayor:
                mayor = matriz1[i][j]
                vector = [i,j]
                ifila = i   
                jcolumna = j
                mayorA = mayor

def suma_zona(matriz):
    global suma
    suma = np.zeros([6,6])
    for a in range(6):
        for s in range(6):
            #suma[1][0] = 3
            #suma[a,0] = suma[a,0] + matriz[a,s]
            #suma[a][0] = 3
            #suma[a][0] = suma[a][0] + matriz1[a][s]
            suma[a,0] = suma[a][0] + matriz1[a][s]
    m_suma[0][0] = suma[0][0]
    m_suma[1][0] = suma[1][0]
    m_suma[2][0] = suma[2][0]
    m_suma[3][0] = suma[3][0]
    m_suma[4][0] = suma[4][0]
    m_suma[5][0] = suma[5][0]
            #m_suma.append(suma[a,0])
            
def cambio(matriz,lista):
    global despachos_sector
    despachos_sector = []
    for z in range(6):
        for m in range(1):
            despachos_sector.append(m_suma[z,m])

def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux

def mayor(lista1,lista2):
    for a in range(len(lista1)- 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)
            
def separador(lista1,lista2):
    for a in range(len(lista1)):
        print('Zona',lista1[a],'-',lista2[a])
        
arch = open('recibidos.txt', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(";")
    fecha = partes[0]
    zona_sector = partes[1]
    cant_items = int(partes[2])
    
    zs = zona_sector.split("-")
    zona = zs[0]
    sector = int(zs[1])
    
    agregar_dato(fechas,fecha)
    agregar_dato(zonas_sectores,zona_sector)
    agregar_dato(cant,cant_items)
    
    columna = agregar_dato(sectores,sector)
    fila = agregar_dato(zonas,zona)
    

    if matriz1[fila][columna] + cant_items >= 100:
       matriz1[fila][columna] = matriz1[fila][columna] + cant_items - 100
       matriz2[fila][columna] += 1
       print('Se realiza un despacho en',zona,sector,'el',fecha)
       
       if sector == 1:
         costo_total += 125
         cant_despachos += 1
       elif sector == 2:
           costo_total += 325
           cant_despachos += 1
       elif sector == 3:
           costo_total += 198
           cant_despachos += 1
       elif sector == 4:
           costo_total += 635
           cant_despachos += 1
       elif sector == 5:
           costo_total += 312
           cant_despachos += 1
       elif sector == 6:
           costo_total += 185
           cant_despachos += 1
           
    else :
        matriz1[fila][columna] += cant_items   
     
    
    
    linea = arch.readline().strip()
    
mayor_pendientes(matriz1)
suma_zona(matriz1)
cambio(m_suma,despachos_sector)
mayor(despachos_sector,zonas)
print('Los envíos por zona-sector en el mes fueron:')
print(matriz2)
print('El costo total de los',cant_despachos,'despachos es',costo_total)
print('Las ubicaciones con la mayor cantidad de items pendientes son:')
print(zonas[ifila],'-',sectores[jcolumna],'con',mayorA)
print('El total de items pendientes por zonas:')
separador(zonas,despachos_sector)