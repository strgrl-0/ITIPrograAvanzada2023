"""
Clase 9 PPT ejercicios,ej1
"""

import numpy as np
distancias = np.zeros([10,10])
arch = open("distancias.txt","r",encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    ori = partes[0].upper()
    dest = partes[1].upper()
    dist = int(partes[2])
    
    if not ori in distancias:
        distancias.append(ori)
    if not dest in distancias:
        distancias.append(dest)
        
    f = distancias.index(ori)
    c = distancias.index(dest)
    
    distancias[f][c] = dist
    
    
arch.close()

