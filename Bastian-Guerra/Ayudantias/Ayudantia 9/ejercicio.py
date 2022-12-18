# """
# Ayudantia 9, ejercicio
# """

import numpy as np

def agregar(lista,elemento):
    lista.append(elemento)

def buscarAgregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)

    
def libre(lista,c,f):
    if lista[c][f] == 0:
        return "Liberada"
    else:
        return "Ocupada"

def precio(valorConsulta,prevision):
        if prevision == "fonasa":
            valor = valorConsulta * 0.85
            return valor
        if prevision == "isapre":
            valor = valorConsulta * 0.70
            return valor

def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux 

sumaa = 0
sumad = 0
sumat = 0
sumas = 0
sumam = 0
sumaal = 0
mayorNombres = []
mayorPrecios = []
bloques = []
doctores = []
previsiones = []
pacientes = []
datosPrev = np.zeros([2,37]) #C = Previsiones, F = Pacientes
horas = np.zeros([6,6]) #C = Bloques, F = Doctores
arch = open("solicitudes.txt","r")
linea = arch.readline().strip().lower()
while linea != "":
    #Divir en partes el archivo
    partes = linea.split(",")
    paciente = partes[0]
    doctor = partes[1]
    bloque = partes[2]
    prevision = partes[3]
    fono = partes[4]
    #Agregar a listas
    buscarAgregar(doctores, doctor)
    buscarAgregar(bloques, bloque)
    #Filas y columnas
    f = buscarAgregar(doctores, doctor)
    c = buscarAgregar(bloques, bloque)
    c1 = buscarAgregar(previsiones, prevision)
    f1 = buscarAgregar(pacientes, paciente)
    #Contador
    datosPrev[c1][f1] += 1
    horas[c][f] += 1
    #Suma por x doctor
    if doctor == "anahis" :
        e = precio(35000, previsiones[0])
        sumaa += e
        buscarAgregar(mayorNombres, doctor)
    if doctor == "daniel" :
        e = precio(35000, previsiones[0])
        sumad += e
        buscarAgregar(mayorNombres, doctor)
    if doctor == "tahira" :
        e = precio(35000, previsiones[0])
        sumat += e
        buscarAgregar(mayorNombres, doctor)
    if doctor == "sofía" :
        e = precio(35000, previsiones[0])
        sumas += e 
        buscarAgregar(mayorNombres, doctor)
    if doctor == "martin" :
        e = precio(35000, previsiones[0])
        sumam += e
        buscarAgregar(mayorNombres, doctor)
    if doctor == "alejandra" :
        e = precio(35000, previsiones[0])
        sumaal += e
        buscarAgregar(mayorNombres, doctor)
    linea = arch.readline().strip().lower()
    
agregar(mayorPrecios, sumas)
agregar(mayorPrecios, sumad)
agregar(mayorPrecios, sumat)
agregar(mayorPrecios, sumaa)
agregar(mayorPrecios, sumam)
agregar(mayorPrecios, sumaal)

#Imprimir bloques ocupados y desocupados
for a in range(0,6):
    for b in range(0,6):
        consulta = libre(horas, b, a)
        print("Doctor:",doctores[a],"Bloque:",bloques[b],"Estado:",consulta)    

#Ordenar listas
for d in range(len(mayorNombres) - 1):
    for e in range(d + 1,len(mayorNombres)):
        if mayorPrecios[d] > mayorPrecios[e]:
            intercambiar(mayorNombres, d, e)
            intercambiar(mayorPrecios, d, e)
 
#Imrimir mayor y menos    
print("El medico que genero mas ingresos fue:",doctores[5],"con",mayorPrecios[5]) 
print("El medico que genero menos ingresos fue:",doctores[0],"con",mayorPrecios[0])    
   



