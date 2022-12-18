"""
Clase 10 PPT ejercicios
"""

"""
NO HICE LA 5 POR QUE SOY TONTITO QWEWQEQWEQWEQWEWQEQWEQWEQWEQWEQW
"""


import numpy as np

#matriz
mtx = np.zeros([8,12])

#Variables
totalMensaje = 0 #Mensajes totales
totalMultimedia = 0 # Mensajes totales archivos multimedia
promMultimedia = 0
mayor = -1 #Mayor cantidad de mensajes
nombreMayor = 0 #Nombre de mayor cantidad mensajes
mesMayor = 0 #Mes mayor cantidad mensajes
promMensual = 0 #Promedio mensual de mensajes
menor = 10**10
sumaMensajes = 0
nombreMenor = 0


#Listas
emisores = []
meses = []
mensajesEnviadosEmisores = []
multi = ["<sticker>","<gif>","<imagen>","<audio>","<video>"]

#Abrir archivo
arch = open("chat.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Dividir en partes
    partes = linea.split(";")
    hora = partes[1]
    emisor = partes[2]
    mensaje = partes[3]
    #Divir fecha
    fecha = partes[0]
    partes = fecha.split("/")
    dia = partes[0]
    mes = partes[1]
    año = partes[2]
    
    #Contador archivos multimedia
    if mensaje in multi:
        totalMultimedia += 1
        
    #Agregar lista 
    if mes not in meses:
        meses.append(mes)
    if emisor not in emisores:
        emisores.append(emisor)
    
    f = emisores.index(emisor)
    c = meses.index(mes)
    
    mtx[f][c] += 1
    
    totalMensaje += 1 #Contador de mensaje
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()

#Conocer el emisor con más mensajes y el mes
f = len(emisores)
c = len(meses)

for i in range(f): #Por i en el rango de la cantidad de emisores(filas) 
    for j in range(c): #por j en el rango de la cantidad de meses(columnas)
    #Lee cada columna de cada fila
        if mtx[i][j] > mayor: #Si la posicion es matriz es mayor se remplaza
            mayor = mtx[i][j]
            nombreMayor = emisores[i] #Guarda posicion de nombre mayor
            mesMayor = meses[j] #Guarda posicion de mes mayor
        


    
        

#Promedios
promMultimedia = (totalMultimedia / totalMensaje) * 100 
promMensual = (totalMensaje / c)
#Imprimir
print("1) La cantidad de mensaje totales fue:",totalMensaje)
print("2) El porcentaje de contenido multimedia fue:",round(promMultimedia,2),"%")
print("3) El Nombre con mas mensajes fue",nombreMayor,"en el mes",mesMayor)
print("4) El promedio mensual fue de",promMensual,"El mes con mas mensajes fue",mesMayor)

