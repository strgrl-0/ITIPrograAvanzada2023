# Diego Martínez
# ejercicio 2 simulacro

def imprimir(a):
    print('\na) Las ventas totales de QX Steam equivalen a',a)
    
def imprimir_2da(a,b,c):
    print('\nb) La combinación que generó mayor ingreso por ventas:',a,'en',b,'con',c)

def imprimir_ultima(a,b,c,d):
    print('\nd) Las personas premiadas por servicio son:')
    for i in range(len(a)):
        indice = c[i]
        print('\t-> El/la mejor en el servicio de',a[i],'es',d[indice],'con',b[i])

import numpy as np

steam = np.zeros([3,10])
operacion = np.zeros([3,10])
trabajadores = np.zeros([10,10])

# Variables
servicios = []
vehiculos = []
mayores_ingresos = []
nombres = []
maximos_nombre = []
indices_nombre = []
ingresos_totales = 0 # 1ra respuesta
mayor = -111
mayor_auto = ''
mayor_servicio = ''

# Creación de la matriz
arch = open('precios.txt')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    servicio = partes[0]
    vehiculo = partes[1]
    precio = int(partes[2])
    
    if servicio not in servicios:
        servicios.append(servicio)
    if vehiculo not in vehiculos:
        vehiculos.append(vehiculo)
        
    f = vehiculos.index(vehiculo)
    c = servicios.index(servicio)
    
    steam[f][c] = precio   
    linea = arch.readline().strip()
arch.close()

# Empieza el codigo

arch = open('servicios.txt')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(';')
    servicio = partes[1]
    vehiculo = partes[2]
    nombre = partes[3]
    
    if nombre not in nombres:
        nombres.append(nombre)
    
    f = vehiculos.index(vehiculo)
    fl = nombres.index(nombre)
    c = servicios.index(servicio)
    
    trabajadores[fl][c] += steam[f][c]
    ingresos_totales += steam[f][c]
    operacion[f][c] += steam[f][c]
    linea = arch.readline().strip()
    
fila = len(vehiculos)
columna = len(servicios)

for i in range(fila):
    for j in range(columna):
        if mayor < operacion[i][j]:
            mayor = operacion[i][j]
            mayor_auto = vehiculos[i]
            mayor_servicio = servicios[j]
            
imprimir(ingresos_totales)    
imprimir_2da(mayor_servicio,mayor_auto,mayor)

print('\nc) Servicios sin demanda:')
for i in range(fila):
    a = []
    s = []
    a.append(vehiculos[i])
    for j in range(columna):
        if operacion[i][j] == 0:    
            s.append(servicios[j])
        else:
            continue
    print('\t',a[0])
    for x in range(len(s)):
        print('\t->',s[x])
        
fila = len(nombres)
columna = len(servicios)

for i in range(columna):
    indice = []
    suma = []
    for j in range(fila):
        suma.append(trabajadores[j][i])
    indice = suma.index(max(suma))
    indices_nombre.append(indice)
    maximos_nombre.append(suma[indice])

imprimir_ultima(servicios,maximos_nombre,indices_nombre,nombres)


