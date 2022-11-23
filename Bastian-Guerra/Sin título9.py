import numpy as np
matriz = np.zeros([8,12])

def buscarAgregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

multimedia = ["<Sticker>", "<GIF>", "<Imagen>", "<Audio>", "<Video>"]
meses = []
nombres = []
arch = open('chat1.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

cont_msj_multi = 0
cont_mensajes = 0
while linea != '':
    partes = linea.split(';')
    fecha = partes[0]
    parte_fecha = fecha.split('/')
    mes = int(parte_fecha[1])
    hora = partes[1]
    emisor = partes[2]
    mensaje = partes[3]
    posF = buscarAgregar(nombres,emisor)
    posC = buscarAgregar(meses,mes)
    matriz[posF,posC] += 1
    if mensaje in multimedia:
        cont_msj_multi += 1
    cont_mensajes += 1
    
    
    linea = arch.readline().strip()
    
porc_msj_multi = round(cont_msj_multi * 100 / cont_mensajes,2)

print('La cantidad de mensajes enviados es de', cont_mensajes)
print('El porcentaje de contenido multimedia es de', porc_msj_multi,'%')
print(nombres,meses)
print(matriz)
