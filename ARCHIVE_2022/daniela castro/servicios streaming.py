servicios = []
meses = []
subscripciones = []
sumas = []
services = []
cancelaciones = []
usuarios = []

vmenor = 0
vmenor1 = 0

import numpy as np
matriz1 = np.zeros([15,12]) #subscripciones
suma = np.zeros([15,12])
cancelaciones1 = np.zeros([15,1])
matriz2 = np.zeros([15,12]) #usuarios a final de año

def buscar_agregar(elemento,lista) :
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def suma_fila(matriz):
    # global suma
    # suma = np.zeros([15,12])
    for i in range (15):
        for j in range (12):
            suma[i,0] = suma[i][0] + matriz1[i][j]
            if j == 11:
                sumas.append(suma[i][0])
    return suma

def porcentaje(lista):
    total = 0
    for v in range(len(lista)):
        total += sumas[v]
    porcentaje = (sumas[0] / total) * 100
    return print(porcentaje,'%')
    

def buscar_mayor(lista):
    global vmayor
    mayor = lista[0]
    for a in range(len(lista)):
        if lista[a] > mayor:
            mayor = lista[a]
            vmayor = a
    return mayor

def buscar_menor(lista):
    global vmenor
    global mes_barrera1
    menor = lista[0]
    for c in range(len(lista)):
        if lista[c] < menor:
            menor = lista[c]
            vmenor = c
        if lista[c] == menor:
            menor1 = lista[c]
            vmenor1 = c
            barrera = matriz1[vmenor][0]
            barrera1 = matriz1[vmenor1][0]
            for f in range (12):
                barrera += matriz1[vmenor][f]
                barrera1 += matriz1[vmenor1][f]
                if barrera > 30000:
                    mes_barrera = meses[f]
                if barrera1 > 30000:
                    mes_barrera1 = meses[f]
                    break
    return print('Los servicios de streaming con menos suscriptores son:\n','*',servicios[vmenor],'con',int(menor),'suscriptores.\nSuperó los 30.000 suscriptores en el mes de',mes_barrera,'\n*',servicios[vmenor1],'con',int(menor1),'suscriptores.\nSuperó los 30.000 suscriptores en el mes de',mes_barrera1)
    # return print(servicios[vmenor],servicios[vmenor1])

def cant_usuarios(matriz):
    for m in range (15):
        matriz2[m,0] = suma[m][0] - cancelaciones1[m][0]
        usuarios.append(int(matriz2[m][0]))
        print(services[m],':',usuarios[m])
    return matriz2

arch = open('suscripciones.txt',encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '' :
    partes = linea.split('-')
    servicio = partes[0]
    mes = partes[1]
    cantidad = int(partes[2]) #cantidad de suscripciones mensual
    
    plataforma = buscar_agregar(servicio, servicios)
    months = buscar_agregar(mes, meses)
    subscripciones.append(cantidad)
    
    matriz1[plataforma][months] += cantidad
    
    linea = arch.readline().strip()
    
suma_fila(matriz1)    
b = buscar_mayor(sumas)
print('El servicio de streaming con más cantidad de suscriptores es',servicios[vmayor],'con',b,'suscriptores')
d = buscar_menor(sumas)
print('El porcentaje que Netflix posee en el mercado es de:')
porcentaje(sumas)

arch1 = open('cancelaciones.txt',encoding = 'utf-8')
linea1 = arch1.readline().strip()

contador = 0

while linea1 != '':
    partes1 = linea1.split('/')
    service = partes1[0]
    cancelacion = int(partes1[1])
    
    buscar_agregar(service, services)
    buscar_agregar(cancelacion, cancelaciones)
    
    cancelaciones1[contador][0] += cancelacion
    contador += 1
    
    linea1 = arch1.readline().strip()

print('La cantidad de usuarios por servicios es:')
cant_usuarios(matriz2)
g = buscar_mayor(cancelaciones)
print('El servicio con mayor cantidad de cancelaciones es',services[vmayor],'con',g)