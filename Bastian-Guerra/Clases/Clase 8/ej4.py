"""
Clase 8 PPT ejercicios,ej4
"""
"Funciones"
#Agregar elementos a una lista
def agregar(lista,parte):
    lista.append(parte)

#Clasiica los riegos dependiendo si son altos,medios o bajos
def clasificarRiesgo(nombre,parte1,parte2,parte3,lista1,lista2,lista3,lista4,lista5,lista6):
    nombre = str(nombre)
    parte2 = int(parte2)
    if parte1 == nombre:
        if parte2 > 75:
            agregar(lista1,parte1)
            agregar(lista4,parte3)
        elif parte2 > 50 and parte2 <= 75:
            agregar(lista2, parte1)
            agregar(lista5,parte3)
        elif parte2 <= 50:
            agregar(lista3, parte1)
            agregar(lista6,parte3)

#Intercambia los valores de las listas de mayor a menor
def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
#Funcion que ordena listas
def ordenar(lista1,lista2,a,b):
    for a in range(len(lista1) - 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)

#Funcion que imprimir el mensaje de cada riesto
def imprimir(mensajeNivel,MensajeRiesgo,separador,nombre,lista1,lista2):
    print(mensajeNivel)
    print(separador)
    for i in range(len(lista1)):
        print(lista1[i],"(",lista2[i],MensajeRiesgo,")")
    print(separador)
    
    
"Progama"
#Variables
texto = "Riesgo ajustado"
separador = "--------------------------"
a = 0
b = 0
nombres = []
riesgo = []
peso = []
alto = []
medio = []
bajo = []
ra = []
rm = []
rb = []
#Abrir archivo
arch = open("ejercicio4.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
#Leer archivo
while linea != "":
    "Partes"
    partes = linea.split(";")
    uno = str(partes[0]) #Nombres
    dos = int(partes[1]) #Riesgo
    tres = float(partes[2]) #Riesgo ajustado
    "Agregar elementos a las listas"
    agregar(nombres,uno)#Agregar nombres a la lista "nombres"
    agregar(riesgo,dos)#Agregar riesgos a la lista "riesgo"
    agregar(peso,tres)#Agregar pesos a la lista "peso"
    "Clasificar riesgos"
    #Manera mejorada
    for i in range(len(nombres)):
        clasificarRiesgo(nombres[i], uno, dos,tres,alto, medio, bajo,ra,rm,rb)
    "Leer nueva linea"
    linea = arch.readline().strip().lower()

"Ordenar elementos de la lista correspondientes a su nombre y riesgo ajustado"
ordenar(ra,alto,a,b)
ordenar(rm,medio,a,b)
ordenar(rb,bajo,a,b)
"Imprimir mensaje"
imprimir("Riesgo Alto", texto, separador, nombres, alto, ra)
imprimir("Riesgo Medio", texto, separador, nombres, medio, rm)
imprimir("Riesgo Bajo", texto, separador, nombres, bajo, rb)





