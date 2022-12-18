"""
Clase 8 PPT Ejercicios,ej4 practica 
"""

#Funciones
def clasificar(nombre,riesgo):
    if riesgo > 75:
        agregar(riesgoAlto,riesgo)
        agregar(nombreAlto,nombre)
        agregar(riesgoAjustadoAlto,riesgoA)
    elif riesgo <= 75 and riesgo > 50:
        agregar(riesgoMedio,riesgo)
        agregar(nombreMedio,nombre)
        agregar(riesgoAjustadoMedio,riesgoA)
    elif riesgo <= 50:
        agregar(riesgoBajo,riesgo)
        agregar(nombreBajo,nombre)
        agregar(riesgoAjustadoBajo,riesgoA)

        
def agregar(lista,elemento):
    lista.append(elemento)

def imprimir(lista1,lista2):
    for i in range(len(lista1)):
        print(lista1[i],lista2[i],"Riesgo ajustado")

def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
def ordenar(lista1,lista2,a,b):
    for a in range(len(lista1) - 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)    

#Variables
a = 0
b = 0
#Listas
nombres = []
riesgos = []
riesgoAjustado = []
riesgoAjustadoAlto = []
riesgoAjustadoMedio = []
riesgoAjustadoBajo = []
riesgoAlto = []
riesgoMedio = []
riesgoBajo = []
nombreAlto = []
nombreMedio = []
nombreBajo = []
#Abrir archivo
arch = open("ejercicio4.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()


while linea != "":
    #Dividir por partes
    partes = linea.split(";")
    nombre = str(partes[0])
    riesgo = int(partes[1])
    riesgoA = float(partes[2])
    #Agregar a listas
    agregar(nombres, nombre)
    agregar(riesgos, riesgo)
    agregar(riesgoAjustado, riesgoA)
    clasificar(nombre, riesgo)
    #Leer nueva linea
    linea = arch.readline().strip().lower()

#Ordenar
ordenar(riesgoAjustadoAlto  ,nombreAlto , a, b)
ordenar(riesgoAjustadoMedio  ,nombreMedio , a, b)
ordenar(riesgoAjustadoBajo ,nombreBajo , a, b)


#Imprimir
print("Riesgo Alto")
print("---------------------------------")
imprimir(nombreAlto, riesgoAjustadoAlto)
print("---------------------------------")
print("Riesgo Medio")
print("---------------------------------")
imprimir(nombreMedio, riesgoAjustadoMedio)
print("---------------------------------")
print("Riesgo Bajo")
print("---------------------------------")
imprimir(nombreBajo, riesgoAjustadoBajo)