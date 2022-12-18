"""
Ej2 Ayudantia
Dadas las siguientes notas almacenadas en un arreglo: [20,15,12,11,8,4,1]
Elimine la nota más baja e imprímala por pantalla. Luego calcule el promedio de notas sin
tener en cuenta la ya eliminada.
"""

def eliminar(lista,elemento):
    lista.remove(elemento)
    
def intercambiar(lista,indice1,indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux
    
def ordenar(lista):
    for a in range(len(lista) - 1):
        for b in range(a + 1,len(lista)):
            intercambiar(lista,a,b)
            
    
lista = [20,15,12,11,8,4,1]
aux = 0

ordenar(lista)
aux = lista[0]
print("La nota mas baja fue y que sera eliminada:",aux)
eliminar(lista,aux)
print("La nueva lista es",lista)


