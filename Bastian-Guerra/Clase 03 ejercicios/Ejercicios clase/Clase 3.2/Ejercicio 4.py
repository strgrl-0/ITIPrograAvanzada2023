"""
Bastian Guerra Valdés, ITI 
"""

n = 0
c = 0
x = float(input("Ingrese un numero: "))

if x == -1:
    print("No se puede realizar el calculo")
else:
    while x != -1:
        if x >= 4:
            c = c + 1
        else:
            n = n + 1
            x = float(input("Ingrese un numero: "))
    else:
        porc = 100 * (c/n)
        print(porc)