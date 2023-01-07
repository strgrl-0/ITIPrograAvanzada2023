"""
Ayudantia 8,ej1

Crea un programa que primero pregunte por una cantidad de alumnos cualquiera,
luego que pregunte por consola los nombres y promedios finales por cada alumno 
especificado. Una vez ingresados los datos,mostrar por pantalla:
a. Los nombres y promedios de los alumnos cuyo promedio final sea mayor o igual a 6,0. 
En caso de que no haya alumnos, mostrar un mensaje notificando esto.
b. El nombre y promedio del alumno con mejor nota.
c. El nombre y promedio del alumno con peor nota.
"""

#Funciones
def agregar(lista,elemento):
    lista.append(elemento)

def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
def menor(lista1,lista2):
    for a in range(len(lista1) - 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] > lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)

            
def mayor(lista1,lista2):
    for a in range(len(lista1) - 1):
        for b in range(a + 1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)

def imprimirIndice(mensaje,lista1,lista2,indice):
    print(mensaje)
    print(lista1[indice])
    print(lista2[indice])
    print("-------------------------------")

def imprimir(mensaje,lista1,lista2):
    print("-------------------------------")
    print(mensaje)
    print(lista1)
    print(lista2)
    print("-------------------------------")

#Funciones
nombres = []
notas = []
mayor6 = []
nombre6 = []

#Cantidad alumnos a evaular
cantidad = int(input("Ingrese la cantidad de alumnos a evaular: "))
#Prueba de error
while cantidad < 0:
    cantidad = int(input("Error,Ingrese la cantidad de alumnos a evaular: "))
#Si alumnos = 0
if cantidad == 0:
    print("Finalizar progama")
    
for i in range(cantidad):
    print("Usted va a ingresar a el estudiante numero:",i + 1)
    alumno = input("Ingrese nombre estudiante: ").lower()
    agregar(nombres,alumno)
    promedio = float(input("Ingrese promedio final: "))
    while promedio < 1.0 or promedio > 7.0:
        promedio = float(input("Error,Ingrese promedio final: "))
    agregar(notas,promedio)
    #Notas mayores a 6
    if promedio >= 6.0:
        agregar(mayor6,promedio)
        agregar(nombre6,alumno)
       
#Imprimir alumnos y notas mayores a 6        
imprimir("Nombres y notas mayores a 6", mayor6, nombre6)
#Ordenar y imprimir alumno con mayor notas
mayor(notas,nombres)
imprimirIndice("Notas y nombre de alumnos con mejor promedio", nombres, notas, 0)
#Ordenar y imprimir alumno con menor notas
menor(notas,nombres)
imprimirIndice("Notas y nombre de alumnos con menor promedio", nombres, notas, 0)


