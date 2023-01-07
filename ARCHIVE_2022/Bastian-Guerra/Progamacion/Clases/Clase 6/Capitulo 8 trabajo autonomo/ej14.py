"""
Ejercicios libro guia Capitulo 8 ,ej 14
"""
def separarNombre(arch):
    arch = open("personas.txt")
    linea = arch.readline().strip()
    partes = linea.split(",")
    uno = partes[0]
    while linea != "":
        partes = linea.split(",")
        uno = partes[0]
        linea = arch.readline().strip()
        print(uno)


arch = open("personas.txt","r",encoding = "utf-8")
separarNombre(arch)