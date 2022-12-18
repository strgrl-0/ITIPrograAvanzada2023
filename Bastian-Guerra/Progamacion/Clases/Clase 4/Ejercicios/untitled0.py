"""
Bastian Guerra ITI
"""

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
pro = (n1 + n2 +n3) / 3

if n1 >= 4.0 and n2 >= 4.0 and n3 >= 4.0:
    print("Todas las notas han sido iguales o mayores a 4.0, su promedio final aumento en 0.5")
    pro = pro + 0.5
    
