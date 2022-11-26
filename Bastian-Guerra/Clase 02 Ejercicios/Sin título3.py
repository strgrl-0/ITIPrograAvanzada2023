# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:23:52 2022

@author: LabCivil2-Pc12
"""

figura = str(input("¿Que figura es? (triangulo, cirgulo o cubo): "))

pi = 3,14

if figura == "triangulo":
    print("¿Cual es su altura y base?")
    altura = float(input("altura: "))
    base = float(input("base: "))
    area_triangulo = base * altura / 2
    print("Su area es: ",area_triangulo)
if figura == "circulo":
    print("¿Cual es su radio?")
    radio = float(input("radio: "))
    area_circulo = pi * (radio ** 2)
    print("Su area es :",area_circulo)
if figura == "cubo":
    print("¿Cuanto mide uno de sus lados?: ")
    lado = float(input("lado:"))
    area_cubo = 6 * (lado**2)
    print("Su area es: ",area_cubo)