"""
Clase 8 PPT ejercicios,ej3
"""

"Funciones"
#Intercambia los valores de las listas de mayor a menor
def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
#Agregar elemento a una lista con 1 parametro
def agregar(lista,uno):
    lista.append(uno)
    
#Agregar elemento a una lista con 3 parametros
def agregar2(lista,uno,dos,tres):
    lista.append(uno + dos + tres)
    
#Calculo de puntajes
def puntaje(nombre,punt,tiempo,penal,num):
    nombre = str(nombre)
    num = int(num)
    punt = (int(tiempo[num]) / 3) + (int(penal[num]))
    return punt

#Imprimir resultados
def imprimir(nombres,puntajes,penal,num,puesto):
        print("El lugar",puesto,"fue para",nombres[num],"con",puntajes[num],"(",penal[num],"Penalizaciones )")
    
"Variables"
#Puntajes
punt = 0
#Listas
nombres = []
penal = []
tiempo = []
puntajes = []
"Progama"
#Abrir archivo
arch = open("ejercicio3.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
#Leer archivo
while linea != "":
    #partir la lista en partes
    partes = linea.split(",")
    uno = str(partes[0]) #Nombre
    dos = int(partes[1]) #tiempo1
    tres = int(partes[2]) #Tiempo2
    cuatro = int(partes[3]) #Tiempo3
    cinco = int(partes[4]) #Penal1
    seis = int(partes[5]) #Penal2
    siete = int(partes[6]) #Penal3
    #Agregar elementos a las listas conrrespondientes
    agregar(nombres,uno) #Lista nombres usando funcion agregar (Dos parametros)
    agregar2(tiempo,dos,tres,cuatro) #Tiempo usando agregar2
    agregar2(penal,cinco,seis,siete) #Penalizacion usando agregar2
    linea = arch.readline().strip().lower()

#Calculo puntajes
for i in range(len(nombres)):
    punt = puntaje(nombres[i],punt, tiempo, penal, i)
    agregar(puntajes,punt)
    
#Ordenar listas
for a in range(len(nombres) - 1):
    for b in range(a + 1,len(nombres)):
        if puntajes[a] > puntajes[b]:
            intercambiar(nombres, a, b)
            intercambiar(puntajes, a, b)
        elif puntajes[a] == puntajes[b]:
            if nombres[a] > nombres[b]:
                intercambiar(nombres, a, b)
                intercambiar(puntajes, a, b)
                
#Imprimir valores
imprimir(nombres, puntajes, penal, 0,1)
imprimir(nombres, puntajes, penal, 1,2)
imprimir(nombres, puntajes, penal, 2,3)

