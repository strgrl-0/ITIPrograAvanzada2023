"""
Clase 7 ejercicios PPT, ej2
"""

def contador(lista,e):
    c = 0
    for i in lista:
        if i == e:
            c += 1
    return c

arch = open("nombres1.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
lista = []
lista2 = []
lista3 = []
c = 0

while linea != "":
    nombre = str(linea)
    lista.append(nombre)
    linea = arch.readline().strip().lower()

for a in lista:
    if a not in lista2:
        lista2.append(a)
          
for b in range(len(lista)):
    x = contador(lista,lista[b])
    lista3.append(x)
    
for c in range(len(lista2)):
    print("Nombre",lista2[c],"Aparece",lista3[c],"cantidad de veces en la lista")       
 


