"""
Simulacro prueba 2,Bastian guerra,ej2
"""

def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux

def mayor(a,b):
    for i in range(len(a)-1):
        for j in range(i + 1,len(a)):
            if a[i] < a[j]:
                intercambiar(b,i,j)
                intercambiar(a,i,j)
            elif a[i] == a[j]:
                if a[i] > a[j]:
                    intercambiar(b,i,j)
                    intercambiar(a,i,j)


import numpy as np


servicioVehiculo = np.zeros([3,8])

#Listas
servicios = []
vehiculos = []
empleados = []
#Variables
total = 0
mayorIngreso = 0
mayor = -1


#Primer archivo
arch = open("precios.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Dividir en partes
    partes = linea.split(",")
    servicio = partes[0]
    vehiculo = partes[1]
    precio = int(partes[2])
    
    #Agregar elementos a listas
    if servicio not in servicios:
        servicios.append(servicio)
    if vehiculo not in vehiculos:
        vehiculos.append(vehiculo)
        
    
    f = vehiculos.index(vehiculo)
    c = servicios.index(servicio)
    
    servicioVehiculo[f][c] += precio
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()

arch.close()

arch = open("servicios.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Divir en partes
    partes = linea.split(";")
    idVenta = partes[0] 
    servicio = partes[1]
    vehiculo = partes[2]
    empleado = partes[3]
    
    if empleado not in empleados:
        empleados.append(empleado)
        
    f = vehiculos.index(vehiculo)
    c = servicios.index(servicio)
    f1 = empleados.index(empleado)
    
    total += servicioVehiculo[f][c]
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()

#Imprimir resultados
print("a) El total de ventas de XQ Team fue de:",total)