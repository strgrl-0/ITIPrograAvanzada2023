# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:11:45 2022

@author: LabCivil2-Pc12
"""

x = int(input("Ingrese primer número entero: "))
y = int(input("Ingrese segundo número entero: "))

if y == 0:
    print("error")    
else:
    division = x / y
    resto = x % y
    division_entera = x // y
    if division == division_entera:
        print("la division es entera: ",int(division))
    else:
        print("la division no es entera su resto es: ",resto)
    if x > y:
        print("El primer valor es mayor: ",x)
    elif x < y:
        print("El segundo valor es mayor: ",y)
    else:
        print("Ambos son iguales, ninguno es mayor: ",x)
        