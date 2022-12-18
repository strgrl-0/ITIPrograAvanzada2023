"""
Clase 8 PPT ejercicios,ej2
"""

def contador(lista,e):
    c = 0
    for i in lista:
        if i == e:
            c += 1
    return c
    

def maximo(lista,mayor):
    mayor = -1
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
    

#Variables contadores
c = 0
#Listas de cada nombre
unicos = []
nombres = []
cantidad = []
#Mayor
mayor = -1

#Abrir archivo
arch = open("ejercicio2.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
#Leer archivo
while linea != "":
    partes = linea.split()
    nombres.append(str(partes[0])) #Agregar txt a una lista
    #Leer nueva linea
    linea = arch.readline().strip().lower()

print("Lista original:",nombres)

#Ordenar lista alfabeticamente
for a in range(len(nombres) - 1):
    for b in range(a + 1,len(nombres)):
        if nombres[a] > nombres[b]:
            aux = nombres[a]
            nombres[a] = nombres[b]
            nombres[b] = aux

#Cantidad de veces que aparece un nombre en la lista nombres
for d in range(len(nombres)):
    x = contador(nombres,nombres[d])
    cantidad.append(x)

#Numero mayor
numeroMayor = maximo(cantidad,mayor)

print("Lista de manera ordenada:",nombres)
print("El numero mayor de repeticiones fue:",nombres[numeroMayor],"con",numeroMayor,"repeticiones") 
