"""
Clase 9 PPT ejercicios,ej2
"""
import numpy as np

def buscarAgregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)

def contador(contador,elemento,lista):
    if elemento in lista:
        contador += 1

#Variables
a1 = 0
b1 = 0
b2 = 0
c3 = 0
c7 = 0
d3 = 0
d8 = 0
f1 = 0
f3 = 0
f5 = 0
#Progama
distancia = np.zeros([10,10])
vehi = []
conductor = []

arch = open("ej2.txt","r",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(";")
    condu = partes[0]
    maqui = partes[1]
    kilo = partes[2]
    
    f = buscarAgregar(vehi, maqui)
    c = buscarAgregar(conductor, condu)
     
    distancia[f,c] += 1

    linea = arch.readline().strip()


print(a1)
  