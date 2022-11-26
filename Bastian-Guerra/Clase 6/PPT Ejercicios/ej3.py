"""
Clase 06 Ejercicios, ej3
"""
a = 3
b = 99

def esPrimo (n):
    x = 1
    c = 0
    while x <= n:
        if n % x == 0:
            c = c + 1
        x = x + 1
    if c == 2:
        return True
    else:
        return False
    
n = int(input("Ingrse el numero a revisar si es primo o no: "))

while a < b:
    entre = esPrimo(a)
    a += 1
    print("Ciclo:",a,entre)

vof = esPrimo(n)
print("Valor ingresado:",n,vof)

