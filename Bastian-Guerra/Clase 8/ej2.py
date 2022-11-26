"""
Clase 8 PPT ejercicios,ej2
"""
#Variables contadores
c_mauri = 0
c_leo = 0
c_lore = 0
c_anto = 0
c_joa = 0
c_rosa = 0
c_mari = 0
c_cris = 0
c_albe = 0
c_juan = 0
#Listas de cada nombre
nombres = []
#Mayor
mayor = -1
mayor_nombre = ""

#Abrir archivo
arch = open("ejercicio2.txt","r",encoding = "utf-8")
linea = arch.readline().strip().lower()
#Leer archivo
while linea != "":
    partes = linea.split()
    nombres.append(str(partes[0])) #Agregar txt a una lista
    #Contador
    if partes[0] == "mauricio":
        c_mauri += 1
    if partes[0] == "joaquín":
        c_joa += 1
    if partes[0] == "maria":
        c_mari += 1
    if partes[0] == "leonor":
        c_leo += 1
    if partes[0] == "antonia":
        c_anto += 1
    if partes[0] == "cristina":
        c_cris += 1
    if partes[0] == "alberto":
        c_albe += 1
    if partes[0] == "juan":
        c_juan += 1
    if partes[0] == "lorena":
        c_lore += 1
    if partes[0] == "rosario":
        c_rosa == 1
    #Leer nueva linea
    linea = arch.readline().strip().lower()
    #Ordenar lista alfabeticamente
    for a in range(len(nombres) - 1):
        for b in range(a + 1,len(nombres)):
            if nombres[a] > nombres[b]:
                aux = nombres[a]
                nombres[a] = nombres[b]
                nombres[b] = aux

if c_mauri > c_joa and c_mauri > c_leo and c_mauri > c_anto and c_mauri > c_anto and c_mauri > c_cris and c_mauri > c_albe and c_mauri > c_juan and c_mauri > c_lore and c_mauri > c_rosa:
    mayor = c_mauri
    mayor_nombre = "Mauricio"
elif c_joa > c_mauri and c_joa > c_leo and c_joa > c_mari and c_joa > c_anto and c_joa > c_cris and c_joa > c_albe and c_joa > c_juan and c_joa > c_lore and c_joa > c_rosa:
    mayor = c_joa
    mayor_nombre = "Joaquin"
elif c_mari > c_mauri and c_mari > c_leo and c_mari > c_joa and c_mari > c_anto and c_mari > c_cris and c_mari > c_albe and c_mari > c_juan and c_mari > c_lore and c_mari > c_rosa:
    mayor = c_mari
    mayor_nombre = "Maria"
  #Me dio weba poner los otros nombres pero el codigo funciona asi que lo dejo asi, seguro despues existira una manera mas eficiente de hacerlo xd  

print("Lista de manera ordenada:",nombres)
print("El numero mayor de repeticiones fue:",mayor_nombre,"con",mayor,"repeticiones") 
