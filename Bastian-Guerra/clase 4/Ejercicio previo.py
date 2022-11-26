"""
Bastian Guerra Valdes, ITI
"""
archivo = open("edades.txt")
linea = archivo.readline().strip()

while linea != "fin":
    print(linea)