# Diego Martínez C7
# ejercicio 1, clase 10

#-----------------------------------FUNCIONES-----------------------------------

def porcentajes_multimedia(a,b):
    total = (a *100)/b
    return total

def imprimir_1(a,b):
    print('\n1)La cantidad de mensajes enviados es de', a)
    print('\n2)El porcentaje de contenido multimdia es de',round(b,2),'%')
    
def imprimir_2(lista1,lista2,lista3,lista4):
    indice = lista1.index(max(lista1))
    indice_2 = lista3.index(max(lista3))
    print('\n3)La(s) persona(s) con más mensajes enviados, con',lista1[indice],'es/son:')
    print('-',lista2[indice])
    print('- Su mes con más mensajes fue',lista4[indice_2],'con',lista3[indice_2])
    
def imprimir_3(a,lista,lista2):
    largo_lista = len(lista)
    total = a/largo_lista
    indice = lista2.index(max(lista2))
    print('\n4)El promedio mensual de mensajes es', total,'y el(los) mes(es) con más mensajes fue(ron):')
    print('-',lista[indice])
    
def imprimir_4(lista1,lista2):
    
    indice = lista2.index(min(lista2)) # 1er menor
    print('\n5)Las dos personas que menos hablan son:')
    print('-',lista1[indice],'con',lista2[indice],'mensajes')
    del lista1[indice]
    del lista2[indice]
    
    indice = lista2.index(min(lista2)) # 2do menor
    print('-',lista1[indice],'con',lista2[indice],'mensajes')
    print('')

#-----------------------------------MATRIZ-----------------------------------

import numpy as np

matriz = np.zeros([100,100])

#-----------------------------------VARIABLES/LITSAS-----------------------------------

emisores = []
meses = []
mensajes_multimedia = ['<Sticker>','<GIF>','<Imagen>','<Audio>','Video>']
mensajes_enviados_emisores = []
mensajes_enviados_meses = []
mensajes_enviados_mayor = []

total_mensajes = 0
total_mensajes_multimedia = 0
suma = 0
suma_2 = 0

#-----------------------------------CODIGO-----------------------------------

arch = open('chat.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split('/') 
    mes = int(partes[1])
    
    if mes not in meses:
        meses.append(mes) 

    partes = linea.split(';')
    emisor = partes[2]
    mensaje = partes[3]
    total_mensajes += 1
    
    for i in mensajes_multimedia:
        if mensaje == i:
            total_mensajes_multimedia += 1
    
    if emisor not in emisores: 
        emisores.append(emisor)
    
    fila = emisores.index(emisor)
    columna = meses.index(mes)
    
    matriz[fila][columna] += 1
    
    linea = arch.readline().strip()
   
f = len(emisores)
c = len(meses)

# 1er ciclo para leer cantidad de mensajes x nombre

for i in range(f+1):
    if i != 0:
        mensajes_enviados_emisores.append(suma)
    suma = 0
    for x in range(c):
        if matriz[i][x].any():
            suma += matriz[i][x]
        else:
            continue

indice_max = mensajes_enviados_emisores.index(max(mensajes_enviados_emisores))
indice_nombre = emisores[indice_max]

# ciclo para leer la cantidad de mensajes enviados x meses del nombre con mayor mensajes

for i in range(c):
    if matriz[indice_max][i].any:
        mensajes_enviados_mayor.append(matriz[indice_max][i])
    else:
        continue
     
# 2 ciclo para leer la cantidad de mensajes x mes

for i in range(c + 1):
    if i != 0:
        mensajes_enviados_meses.append(suma_2)
    suma_2 = 0
    for x in range(f):
        if matriz[x][i].any():
            suma_2 += matriz[x][i]
        else:
            continue  

#-----------------------------------SALIDA-----------------------------------

print('')
print('---------------------------------------------------------------------------------------------')    
potcentaje_mensajes_multimedia = porcentajes_multimedia(total_mensajes_multimedia,total_mensajes) # variable respuesta 2
imprimir_1(total_mensajes,potcentaje_mensajes_multimedia)
imprimir_2(mensajes_enviados_emisores,emisores,mensajes_enviados_mayor,meses) 
imprimir_3(total_mensajes,meses,mensajes_enviados_meses)
imprimir_4(emisores,mensajes_enviados_emisores)
print('---------------------------------------------------------------------------------------------')   