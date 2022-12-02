"""
Simulacro prueba ej2
"""

def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

import numpy as np

servicioVehiculo = np.zeros([8,3])
ventas = np.zeros([8,3])
empleadoServicio = np.zeros([6,8])

#Listas
servicios = []
vehiculos = []
empleados = []

#Variables
totalVentas = 0 #Pregunta numero 1
mayor = -10**10 #Pregunta numero 2
autoMayor = 0 #Pregunta numero 2
servicioMayor = 0 #Pregunta numero 2

#Primer archivo
arch = open("precios.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Dividir en partes
    partes = linea.split(",")
    servicio = partes[0]
    vehiculo = partes[1]
    precio = int(partes[2])
    
    #Agregar a listas
    agregar(servicios,servicio)
    agregar(vehiculos,vehiculo)


    f = servicios.index(servicio)
    c = vehiculos.index(vehiculo)

    servicioVehiculo[f,c] += precio
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()

arch.close()

#Segundo archivo
arch = open("servicios.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Dividir en partes
    partes = linea.split(";")
    idVenta = partes[0]
    servicio = partes[1]
    vehiculo = partes[2]
    empleado = partes[3]
    
    #Agregar a listas
    agregar(empleados,empleado)
    
    #Filas y columnas            
    f = servicios.index(servicio)
    c = vehiculos.index(vehiculo)
    f1 = empleados.index(empleado)

    empleadoServicio[f1,f] += servicioVehiculo[f,c]
    
    #Suma total ventas
    totalVentas += servicioVehiculo[f,c]
    #Matriz de ventas
    ventas[f][c] += servicioVehiculo[f,c]
    #Calculo mayor combinacion ingreso
    if ventas[f,c] > mayor:
        mayor = ventas[f,c]
        autoMayor = vehiculos[c]
        servicioMayor = servicios[f]
    
    #Leer nueva linea    
    linea = arch.readline().strip().lower()

filas1 = len(empleados)
filas = len(servicios)
columnas = len(vehiculos)


            
print("----------------------------------")          
#Imprimir resultados
print("A) Total de ventas realizadas:",totalVentas)
print("B) La combinacion que genero mas ingresos fue:",servicioMayor,autoMayor,"con",mayor,"$")
print("C) Servicios sin demanda")
for i in range(columnas):
    print("----------------------------------")
    print("Considere eliminar en",vehiculos[i])
    for j in range(filas):
        if ventas[j,i] == 0:
            print(servicios[j])
            
print("----------------------------------")
            
for i in range(filas):
    listaMayor = []
    mayorEmpleado = -10*10
    empleadorMayor = 0
    print("El mejor empleado en el servicio de",servicios[i])
    if empleadoServicio[j,i] > mayorEmpleado:
        mayorEmpleado = empleadoServicio[j,i]
        empleadoMayor = empleados[j]
        print(mayorEmpleado,empleadoMayor)