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

def puntaje(parte,nombre,punt,tiempo,penal,num):
    nombre = str(nombre)
    num = int(num)
    if parte == nombre:
        punt = (int(tiempo[num]) / 3) + (int(penal[num]))
    return punt

def imprimir(nombres,puntajes,penal,num):
    print("El lugar fue para",nombres[num],"con",puntajes[num],"(",penal[num],"Penalizaciones )")
    
"Variables"
#Puntajes
punt_joa = 0
punt_albe = 0
punt_anto = 0
punt_juan = 0
punt_cris = 0
punt_leo = 0
punt_lore = 0
punt_mari = 0
punt_mau = 0
punt_rosa = 0
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
    #Calculo de puntajes
    if uno == "joaquín":
        punt_joa = (int(tiempo[0]) / 3) + (int(penal[0]))
        agregar(puntajes,punt_joa)
    if uno == "mauricio":
        punt_mau = (int(tiempo[1]) / 3) + (int(penal[1]))
        agregar(puntajes,punt_mau)
    if uno == "maría":
        punt_mari = (int(tiempo[2]) / 3) + (int(penal[2]))
        agregar(puntajes,punt_mari)
    if uno == "leonor":
        punt_leo = (int(tiempo[3]) / 3) + (int(penal[3]))
        agregar(puntajes,punt_leo)
    if uno == "antonia":
        punt_anto = (int(tiempo[4]) / 3) + (int(penal[4]))
        agregar(puntajes,punt_anto)
    if uno == "cristina":
        punt_cris = (int(tiempo[5]) / 3) + (int(penal[5]))
        agregar(puntajes,punt_cris)
    if uno == "alberto":
        punt_albe = (int(tiempo[6]) / 3) + (int(penal[6]))
        agregar(puntajes,punt_albe)
    if uno == "juan":
        punt_juan = (int(tiempo[7]) / 3) + (int(penal[7]))
        agregar(puntajes,punt_juan)
    if uno == "lorena":
        punt_lore = (int(tiempo[8]) / 3) + (int(penal[8]))
        agregar(puntajes,punt_lore)
    if uno == "rosario":
        punt_rosa = (int(tiempo[9]) / 3) + (int(penal[9]))   
        agregar(puntajes,punt_rosa)
    linea = arch.readline().strip().lower()


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
imprimir(nombres, puntajes, penal, 0)
imprimir(nombres, puntajes, penal, 1)
imprimir(nombres, puntajes, penal, 2)

