"""
Bastian Guerra Valdes,ITI,Clase 2,Ejercicio 3
"""

"""
Pregunta por una figura geométrica (Triángulo, Circulo o Cubo) 
y luego dependiendo de cuál sea pregunta por
los elementos necesarios para calcular el área.
"""

print("--------------------------------------")
fig = str(input("¿Que figura es? (triangulo,circulo o cubo): "))
print("---------------------------------------")
#Numero pi
pi = float(3.14)

if fig == "triangulo":
    print("¿Cual es su altura y base?: ")
    alt_tri = float(input("Altura: "))
    base_tri = float(input("Base: "))
    area_tri = (alt_tri * base_tri) / 2
    print("El area del triangulo es:",area_tri)

if fig == "circulo":
    print("¿Cual es su radio?: ")
    radio_cir = float(input("radio: "))
    area_cir = float(pi * (radio_cir ** 2))
    print("El area del circulo es:",area_cir)

if fig == "cubo":
    print("¿Cual es la medida de uno de sus lados?: ")
    lado_cubo = float(input("lado: "))
    area_cubo = (lado_cubo * 6) 
    print("El area del cubo es:",area_cubo)