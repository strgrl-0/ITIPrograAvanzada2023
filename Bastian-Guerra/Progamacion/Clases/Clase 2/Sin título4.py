# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:29:40 2022

@author: LabCivil2-Pc12
"""

p1 = float(input("Ingrese nota prueba 1: "))
p2 = float(input("Ingrese nota prueba 2: "))
p3 = float(input("Ingrese nota prueba 3: "))
c1 = float(input("Ingrese nota corta 1: "))
c2 = float(input("Ingrese nota corta 2: "))
t1 = float(input("Ingrese nota taller: "))
cantidad_t = float(input("Ingrese cantidad de alumnos en el taller: "))

pc = (c1 + c2) / 2
nc = (p1 + p2 + p3 + pc) / 4
d = 0

if cantidad_t != 2 or cantidad_t != 3:
    print("Los alumnos eran minimo 2 y maximo 3 en taller")
else:
    if nc >= 3.5 and nc <= 3.9:
        print("Se va a recalificacion")
        recalificacion = float(input("Nota de recalificacion: "))
        nfc = (nc + recalificacion) / 2
        if nfc != 0:
            setenta = nfc * 0.7
            treinta = d * 0.3
        if nc >= 4:
            print("Aprobo el ramo con un promedio de: ",nc)
        else: 
            print("No aprobo el ramo con un promedio de: ",nc)
