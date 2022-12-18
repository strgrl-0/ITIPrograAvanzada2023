"""
Ayudantia 7,j4
Según el archivo llamado “animales” indique la cantidad de veces que se repite cada
animal en el archivo y además imprima al animal que más aparece en el mismo.
"""


"""
Esta incompleto por que soy tonto
"""

def cantidad(lista,elemento):
    c = 0
    if elemento in lista:
        c += 1
    return c


def agregar(lista,elemento):
    lista.append(elemento)    
    
lista = []
lista1 = []
lista2 = []
animal = ""
c = 0

arch = open("animales.txt","r",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    c = 0
    partes = linea.split()
    uno = partes[0]
    agregar(lista,uno)
    linea = arch.readline().strip()

    for a in range(len(lista) - 1):
        for b in range(a + 1,len(lista)):
            cantidad(lista1,uno)
            agregar(lista1, c)
  
print(lista1)
        

