"""
Clase 7 ejercicios PPT, ej1
"""

arch = open("nombres1.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
lista = []
lista2 = []

while linea != "":
    nombre = str(linea)
    lista.append(nombre)
    linea = arch.readline().strip().lower()
 
for i in lista:
    if i not in lista2:
        lista2.append(i)
 
    
print("Lista original",lista)
print("Lista resultante",lista2)