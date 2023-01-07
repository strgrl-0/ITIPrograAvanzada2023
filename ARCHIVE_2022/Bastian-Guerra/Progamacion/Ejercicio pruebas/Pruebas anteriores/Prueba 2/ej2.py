"""
Prueba 2,ej2 
"""
import numpy as np

def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

def mayorMenorServicio(filas,columnas):
    lista = []
    mayor = -1
    menor = 100**100
    for a in range(columnas):
        suma = 0
        for b in range(filas):
            suma += serviciosMeses[b,a] 
        if suma > mayor:
            mayor = suma
            servicioMayor = servicios[a]
        if suma < menor:
            menor = suma
            servicioMenor = servicios[b]
    agregar(lista,mayor)
    agregar(lista,servicioMayor)
    agregar(lista,menor)
    agregar(lista,servicioMenor)
    return lista



#Matrices
serviciosMeses = np.zeros([12,15])
#Variables
total = 0
netflix = 0
mayorCancelacion = -1
servicioCancelacion = 0
#Listas
servicios = []
meses = []
cantidades = []

"""PRIMER ARCHIVO"""


#Abrir archivo
arch = open("suscripciones.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

#Leer archivo
while linea != "":
    #Dividir partes
    partes = linea.split("-")
    servicio = partes[0]
    mes = partes[1]
    cantidad = int(partes[2])
    
    agregar(servicios,servicio)
    agregar(meses,mes)
    
    f = meses.index(mes)
    c = servicios.index(servicio)

    serviciosMeses[f,c] += cantidad
    
    #Cantidad total susciptores
    total += cantidad
    #Suma total suscriptores Netflix
    if servicio == "netflix":
        netflix += cantidad
    
    #Nueva linea
    linea = arch.readline().strip().lower()

arch.close()
filas = len(meses)
columnas = len(servicios)

"""Imprimir resultados primera parte"""
#Pregunta 1
print("-------------------------------------")
p12 = mayorMenorServicio(filas,columnas)
print("1) El servicio con más suscriptores es:")
print(p12[1],"con",p12[0],"suscriptores")
print("-------------------------------------")
#Pregunta 2
print("2) El los servicios con menos sucriptores:")
print(p12[2],"con",p12[3],"suscriptores")
print("-------------------------------------")
#Pregunta 3
print("3) El porcentaje que cubre Netflix en el mercado es:")
print(round(netflix / total * 100,2),"%")
print("-------------------------------------")



"""SEGUNDO ARCHIVO"""

#Abrir archivo
arch = open("cancelaciones.txt",encoding = "utf-8")
linea = arch.readline().strip().lower()

#Leer archivo
while linea != "":
    #Dividir partes
    partes = linea.split("/")
    servicio = partes[0]
    cantidad = int(partes[1])

    agregar(cantidades,cantidad)
 
    #Nueva linea
    linea = arch.readline().strip().lower()

"""IMPRIMIR RESULTADOS SEGUNDA PARTE"""
#Pregunta 4
print("4) La cantidad de usuarios por servicios es:")
for a in range(columnas):
    suma = 0
    for b in range(filas):
        suma += serviciosMeses[b,a]
    if cantidades[a] > mayorCancelacion:
        mayorCancelacion = cantidades[a]
        servicioCancelacion = servicios[a]
    suma = suma - cantidades[a]
    print(servicios[a],":",suma)  

print("El servicio con mayor cantidad de cancelaciones es",servicioCancelacion,"con",mayorCancelacion)
    
    
    
    
    