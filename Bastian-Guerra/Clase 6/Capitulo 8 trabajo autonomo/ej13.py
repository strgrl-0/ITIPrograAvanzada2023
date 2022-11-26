"""
Ejercicios libro guia Capitulo 8 ,ej 13
"""

def suma(arch):
    suma = 0
    arch = open("numeros.txt")
    linea = arch.readline().strip()
    while linea != "":
        linea = int(linea)
        suma += linea
        linea = arch.readline().strip()
    return suma

def cantidad(arch):
    c = 0
    arch = open("numeros.txt")
    linea = arch.readline().strip()
    while linea != "":
        c += 1
        linea = arch.readline().strip()
    return c

arch = open("numeros.txt") #Abrir archivo de texto con numeros en su interior
t = suma(arch) #Suma total
contador = cantidad(arch)
prom = t / contador
print("Suma total de los numeros:",t) #Imprime la suma
print("Cantidad de lineas::",contador) #Imprime cantidad de lineas
print("Valor promedio de los numeros del archivo:",prom)



