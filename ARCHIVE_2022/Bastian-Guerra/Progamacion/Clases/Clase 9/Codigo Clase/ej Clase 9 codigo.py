import numpy as np

def buscarAgregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)
    
    
visitas = np.zeros([10,10])
paises = []
nombres = []
#Abrir archivo
arch = open("visitas.txt")
linea = arch.readline().strip().lower()
#leer archivo
while linea != "":
    partes = linea.split(",")
    nombre = partes[0]
    pais =  partes[1]
    
    f = buscarAgregar(nombres,nombre)
    c = buscarAgregar(paises,pais)
    
    visitas[f][c] += 1
    
    linea = arch.readline().strip().lower()

print(nombres)
print(paises)
print(visitas)