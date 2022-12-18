# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:53:12 2022

@author: LabCivil1-Pc1
"""
arch = open("ejercicio1.txt", encoding='utf-8')
val = []
linea = arch.readline().strip()
while linea != "":
    partes = linea.split()
    val.append(int(partes[0]))
    linea = arch.readline().strip()
for i in range(len(val)):
    for j in range(i,len(val)):
        if val[j] > val[i]:
            aux = val[j]
            val[j] = val[i]
            val[i] = aux
print(val[0:3])


    

    




        
    
    