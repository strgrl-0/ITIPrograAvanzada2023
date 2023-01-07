"""
Libro guia, cap 6, ej 3
"""
arch = open("nacimientos.txt", "r")

linea = arch.readline().strip()
cont = 0

while linea != "":
    partes = linea.split(",")
    nombre = partes [0] 
    ciudad = partes [1]
    a = partes [2]
    cont += 1
    print("Esta informacion esta en la linea de codigo:",cont)
    print("Nombre", nombre)
    print("Ciudad", ciudad)
    print("Año", a)
    linea = arch.readline().strip()

print("La cantidad de lineas de codigo son:",cont)
