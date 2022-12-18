"""
Pruebas invierno, prueba 2, ej2
"""
import numpy as np

#Funciones

def agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)

#Matrices
stock = np.zeros([5,3])
stock2 = np.zeros([5,3])
precioPiezas = np.zeros([5,3])
#Variables
sumaAlta = 0
sumaMedia = 0
sumaBaja = 0
#Listas
piezas = []
gamas = []


"""EJECUCION PROGAMA"""

#Abrir archivo
arch = open("stock.txt",encoding = "utf-8")
linea = arch.readline().strip()

#Lectura archivo
while linea != "":
    #Dividir partes
    partes = linea.split(",")
    pieza = partes[0]
    cantidad = int(partes[1])
    gama = partes[2]
    precio = int(partes[3])
    
    #Agregar a listas
    agregar(piezas,pieza)
    agregar(gamas,gama)
    
    #Filas y columnas
    f = piezas.index(pieza)
    c = gamas.index(gama)
    
    #Agregar a matrices
    stock[f,c] += cantidad
    stock2[f,c] += cantidad
    precioPiezas[f,c] = precio
    
    #Leer nueva linea
    linea = arch.readline().strip()

arch.close()
print("1) Ordenes no validas:")

#Abrir archivo
arch = open("orden_compra.txt",encoding = "utf-8")
linea = arch.readline().strip()

#Lectura archivo
while linea != "":
    #Dividir partes
    partes = linea.split(",")
    oc = partes[0]
    pieza = partes[1]
    cantidad = int(partes[2])
    gama = partes[3]
        
    #Filas y columnas
    f = piezas.index(pieza)
    c = gamas.index(gama)
    
    #Ordenes de compra a la matriz de stock
    stock[f,c] -= cantidad
 
    #Ordenes no procesadas
    if cantidad > 15: #No supe hacer cuando no hay stock suficiente para la cantidad
        print("orden",oc,"no se puede procesar")   
    elif gama == "alta":
        sumaAlta  += precioPiezas[f,c] * cantidad
    elif gama == "media":
       sumaMedia  += precioPiezas[f,c] * cantidad
    elif gama == "baja":
       sumaBaja  += precioPiezas[f,c] * cantidad

    #Leer nueva linea
    linea = arch.readline().strip()

#Filas y columnas para recorrer las matrices
filas = len(piezas)
columnas = len(gamas)

#Pregunta 2
print("2) Ingresos")
print("- alta:",sumaAlta)
print("- media:",sumaMedia)
print("- baja:",sumaBaja)

#Pregunta 3
print("3) reposicion de productos")
for a in range(filas):
    for b in range(columnas):
        if stock[a,b] < 20:
            print("Reponer",piezas[a],"de gama",gamas[b])
            
         
            
            
            
        