"""
Simulacro prueba ej2
"""
import numpy as np #Importar numpy

def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

def mayorIngreso(filas,columnas):
    mayor = -1
    categoriaMayor = 0
    servicioMayor = 0
    for a in range(filas):
        for b in range(columnas):
            if ventas[a,b] > mayor:
               mayor = ventas[a,b]
               categoriaMayor = categorias[b]
               servicioMayor = servicios[a]
    print("b) La combinacion que genero mayor ingreso por ventas fue:",servicioMayor,categoriaMayor,"con",mayor) 

def sinDemanda(filas,columnas):
    for a in range(columnas):
        print("En",categorias[a],"Considere eliminar")
        print("-----------------")
        for b in range(filas):
            if ventas[b,a] == 0:
                print(servicios[b])
        print("-----------------")
            

#Matrices
servicioCategoria = np.zeros([8,3])
ventas = np.zeros([8,3])
ventasEmpleados = np.zeros([6,8])

#Listas
servicios = []
categorias = []
empleados = []

#Variables
ventasTotal = 0 #Pregunta 1

#Abrir primer archivo
arch = open("precios.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

while linea != "":
    #Dividir en partes 
    partes = linea.split(",")
    servicio = partes[0]
    categoria = partes[1]
    precio = int(partes[2])
    
    #Agregar listas
    agregar(servicios,servicio)
    agregar(categorias,categoria)
    
    #Agregar matriz
    f = servicios.index(servicio)
    c = categorias.index(categoria)
    
    servicioCategoria[f,c] += precio
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()
    
#Cerrar primer archivo
arch.close()

#Abrir nuevo archivo
arch = open("servicios.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

#Lectura archivo
while linea != "":
    #Dividir en partes 
    partes = linea.split(";")
    idVenta = int(partes[0])
    servicio = partes[1]
    categoria = partes[2]
    empleado = partes[3]
    
    #Agregar listas
    agregar(empleados,empleado)
    
    #Agregar matriz
    f = servicios.index(servicio)
    c = categorias.index(categoria)
    f1 = empleados.index(empleado)
    
    #Ventas totales
    ventasTotal += servicioCategoria[f,c] #Pregunta 1
    
    #Matrices
    ventas[f,c] += servicioCategoria[f,c] #Ventas de cada categoria y servicio
    ventasEmpleados[f1,f] += servicioCategoria[f,c]
    
    #Leer nueva linea
    linea = arch.readline().strip().lower()

#Cerrar archivo
arch.close()

filas = len(servicios)
filas1 = len(empleados)
columnas = len(categorias)


""" IMPRIMIR RESULTADOS"""
#Pregunta 1
print("a) Las ventas totales de XQ Steam equivales a",ventasTotal,"pesos")
#Pregunta 2
print(mayorIngreso(filas,columnas))
#Pregunta 3
print(sinDemanda(filas,columnas))
#Pregunta 4
print("d) Las personas premiadas por servicio son:")
for a in range(filas):
    mayor = -1
    mayorEmpleado = 0
    for b in range(filas1):
        if ventasEmpleados[b,a] > mayor:
            mayor = ventasEmpleados[b,a]
            mayorEmpleado = empleados[b]
    print("El/la mejor en el servicio de",servicios[a],"es",mayorEmpleado,"con",mayor)